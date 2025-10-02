# -*- coding: utf-8 -*- {{{
# ===----------------------------------------------------------------------===
#
#                 Installable Component of Eclipse VOLTTRON
#
# ===----------------------------------------------------------------------===
#
# Copyright 2022 Battelle Memorial Institute
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# ===----------------------------------------------------------------------===
# }}}

import json

from collections import defaultdict
from datetime import timedelta
from enum import Enum
from pydantic import BaseModel
from typing import Any, Union, Iterable
from treelib import Tree, Node
from treelib.exceptions import DuplicatedNodeIdError, NodeIDAbsentError

from volttron.client.known_identities import CONFIGURATION_STORE

import re
from os.path import normpath

import logging
_log = logging.getLogger(__name__)


class TopicNode(Node):
    def __init__(self, tag=None, identifier=None, expanded=True, data=None, segment_type='TOPIC_SEGMENT', topic=''):
        super(TopicNode, self).__init__(tag, identifier, expanded, data)
        self.data: dict[str, Any] = data if data else {}
        self.data['segment_type'] = segment_type
        self.data['topic'] = topic

    @property
    def segment_type(self):
        return self.data['segment_type']

    @property
    def topic(self):
        return self.data['topic']

    def is_segment(self):
        return True if self.segment_type == 'TOPIC_SEGMENT' else False


class TopicTree(Tree):
    def __init__(self, topic_list=None, root_name='root', node_class=None, *args, **kwargs):
        node_class = node_class if node_class else TopicNode
        super(TopicTree, self).__init__(node_class=node_class, *args, **kwargs)
        if topic_list:
            self._from_topic_list(topic_list, root_name)
        else:
            self.create_node(root_name, root_name).data['segment_type'] = 'TOPIC_ROOT'

    def _from_topic_list(self, topic_list, root_name):
        tops = [t.split('/') for t in topic_list]
        if all([top[0] == root_name for top in tops]):
            [top.pop(0) for top in tops]
        self.create_node(root_name, root_name).data['segment_type'] = 'TOPIC_ROOT'
        for top in tops:
            parent = root_name
            for segment in top:
                nid = '/'.join([parent, segment])
                try:
                    self.create_node(segment, nid, parent=parent)
                except DuplicatedNodeIdError:
                    pass
                parent = nid

    def add_node(self, node, parent=None):
        super(TopicTree, self).add_node(node, parent)
        node.data['topic'] = node.identifier[(len(self.root) + 1):]
        return node

    # TODO: Should this actually be get_child_topics() where topics or routes are returned with wildcards?
    def get_children_dict(self, sub_root_node_id: Union[list, str], include_root: bool = True,
                          prefix: str = '', replace_topic: str = None) -> dict:
        sub_root_node_id = sub_root_node_id if type(sub_root_node_id) is list else [sub_root_node_id]
        level_dict = defaultdict(set)
        for r_id in sub_root_node_id:
            for d in self.children(r_id):
                try:
                    if replace_topic:
                        if include_root:
                            level_dict[d.tag].add('/'.join([self.root, replace_topic, d.tag]))
                        else:
                            level_dict[d.tag].add('/'.join([replace_topic, d.tag]))
                    else:
                        if include_root:
                            level_dict[d.tag].add(d.identifier)
                        else:
                            level_dict[d.tag].add(d.identifier.split('/', 1)[1])
                except NodeIDAbsentError as e:
                    return {}
        ret_dict = {}
        for k, s in level_dict.items():
            if len(s) > 1:
                ret_dict[k] = sorted([normpath('/'.join([prefix, v])) for v in s])
            else:
                ret_dict[k] = normpath('/'.join([prefix, s.pop()]))
        return ret_dict

    def resolve_query(self, topic_pattern: str = '', regex: str = None, exact_matches: Iterable = None,
                      return_leaves=False) -> Iterable:
        def clipping(topic_parts, nids=None):
            nids = nids if nids else []
            if topic_parts:
                part = topic_parts.pop(0)
                if part:
                    if not nids:
                        return clipping(topic_parts, [part]) if self.get_node(part) else nids
                    else:
                        joined_nids = [self.get_node('/'.join([c.identifier, part])).identifier
                                       for n in nids for c in self.children(n)]
                        return clipping(topic_parts, joined_nids)
                else:
                    return nids
            else:
                return [l.identifier for n in nids for l in self.leaves(n)] if return_leaves else nids

        if not topic_pattern:
            # If None or empty string, default to "self.root"
            topic_pattern = self.root
        elif not topic_pattern.startswith(self.root):
            topic_pattern = '/'.join([self.root, topic_pattern])

        regex = re.compile(regex) if regex else None
        topic_nids = clipping([part.strip('/') for part in topic_pattern.split('/-') if part != '']) if topic_pattern else []
        if topic_nids and exact_matches:
            nodes = (self.get_node(n) for n in topic_nids if n in exact_matches and (not regex or regex.search(n)))
        elif topic_nids and not exact_matches:
            nodes = (self.get_node(n)  for n in topic_nids if not regex or regex.search(n))
        elif not topic_nids and exact_matches:
            nodes = (self.get_node(n) for n in exact_matches if (not regex or regex.search(n)) and self.contains(n))
        else:
            nodes = self.filter_nodes(lambda n: regex.search(n.identifier)) if regex else []
        return nodes

    def prune(self, topic_pattern: str = None, regex: str = None, exact_matches: Iterable = None, *args, **kwargs):
        if topic_pattern:
            pattern = re.compile(topic_pattern.replace('-', '[^/]+') + '(/|$)')
            nids = [n.identifier for n in self.filter_nodes(lambda x: pattern.search(x.identifier))]
        else:
            nids = list(self.expand_tree())
        if regex:
            regex = re.compile(regex)
            nids = [n for n in nids if regex.search(n)]
        if exact_matches:
            nids = [n for n in nids if n in exact_matches]
        pruned = self.__class__(topic_list=nids, root_name=self.root, *args, **kwargs)
        for nid in [n.identifier for n in pruned.all_nodes()]:
            old = self.get_node(nid)
            pruned.update_node(nid, data=old.data)
        return pruned

    def get_matches(self, topic, return_nodes=True):
        pattern = topic.replace('-', '[^/]+') + '$'
        nodes = self.filter_nodes(lambda x: re.match(pattern, x.identifier))
        if return_nodes:
            return list(nodes)
        else:
            return [n.identifier for n in nodes]

    def to_json(self, with_data=False, sort=True, reverse=False):
        """To format the tree in JSON format."""
        def custom_encoder(obj):
            if isinstance(obj, BaseModel):
                return obj.model_dump()
            if isinstance(obj, Enum):
                return obj.value
            if isinstance(obj, timedelta):
                return obj.total_seconds()
            return json.JSONEncoder().default(obj)

        return json.dumps(self.to_dict(with_data=with_data, sort=sort, reverse=reverse), default=custom_encoder)


class DeviceNode(TopicNode):
    def __init__(self, tag=None, identifier=None, expanded=True, data=None, segment_type='TOPIC_SEGMENT', topic=''):
        super(DeviceNode, self).__init__(tag, identifier, expanded, data, segment_type, topic)

    def is_point(self):
        return True if self.segment_type == 'POINT' else False

    def is_device(self):
        return True if self.segment_type == 'DEVICE' else False


class DeviceTree(TopicTree):
    def __init__(self, topic_list=None, root_name='devices', assume_full_topics=False,  *args, **kwargs):
        super(DeviceTree, self).__init__(topic_list=topic_list, root_name=root_name, node_class=DeviceNode,
                                         *args, **kwargs)
        if assume_full_topics:
            for n in self.leaves():
                n.data['segment_type'] = 'POINT'
            for n in [self.parent(l.identifier) for l in self.leaves()]:
                n.data['segment_type'] = 'DEVICE'

    def points(self, nid=None):
        if nid is None:
            points = [n for n in self._nodes.values() if n.is_point()]
        else:
            points = [self[n] for n in self.expand_tree(nid) if self[n].is_point()]
        return points

    def devices(self, nid=None):
        if nid is None:
            points = [n for n in self._nodes.values() if n.is_device()]
        else:
            points = [self[n] for n in self.expand_tree(nid) if self[n].is_device()]
        return points

    # TODO: Getting points requires getting device config, using it to find the registry config,
    #  and then parsing that. There is not a method in config.store, nor in the platform.driver for
    #  getting a completed configuration. The configuration is only fully assembled in the subsystem's
    #  _initial_update method called when the agent itself calls get_configs at startup. There does not
    #  seem to be an equivalent management method, and the code for this is in the agent subsystem
    #  rather than the service (though it is reached through the service, oddly...
    @classmethod
    def from_store(cls, platform, rpc_caller):
        # TODO: Duplicate logic for external_platform check from VUIEndpoints to remove reference to it from here.
        kwargs = {'external_platform': platform} if 'VUIEndpoints' in rpc_caller.__repr__() else {}
        devices = rpc_caller(CONFIGURATION_STORE, 'manage_list_configs', 'platform.driver', **kwargs)
        devices = devices if kwargs else devices.get(timeout=5)
        devices = [d for d in devices if re.match('^devices/.*', d)]
        device_tree = cls(devices)
        for d in devices:
            dev_config = rpc_caller(CONFIGURATION_STORE, 'manage_get', 'platform.driver', d, raw=False, **kwargs)
            # TODO: If not AsyncResponse instead of if kwargs
            dev_config = dev_config if kwargs else dev_config.get(timeout=5)
            reg_cfg_name = dev_config.pop('registry_config')[len('config://'):]
            data = {'config': dev_config, 'segment_type': 'DEVICE'}
            device_tree.update_node(d, data=data)
            registry_config = rpc_caller('config.store', 'manage_get', 'platform.driver',
                                         f'{reg_cfg_name}', raw=False, **kwargs)
            registry_config = registry_config if kwargs else registry_config.get(timeout=5)
            for pnt in registry_config:
                point_name = pnt.pop('Volttron Point Name')
                n = device_tree.create_node(point_name, f"{d}/{point_name}", parent=d, data=pnt)
                n.data['segment_type'] = 'POINT'
        return device_tree
