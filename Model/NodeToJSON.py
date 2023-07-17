import json

from Model.Node import *

class NodeToJSON:

    node = Node('', '')

    def __init__(self, node):
        self._node = node

    def toJson(self):
        with open("data_nodes_json", "w") as write_file:
            json.dump(self._node, write_file)