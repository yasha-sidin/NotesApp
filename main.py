from Model.Node import *
from Model.NodeToJSON import NodeToJSON

node = Node("Test", "NJNHYGUYBBIIUHHIBIUBUI")
print(Node.getheader(node), Node.getbody(node))

nodejson = NodeToJSON(node)

nodejson.toJson()