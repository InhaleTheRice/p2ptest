from api.createNode import createNode

node1 = createNode('127.0.0.1', 4208)
node2 = createNode('127.0.0.1', 4209)

node1.connect_with_node('127.0.0.1', 4209)

packet = {}

packet['message'] = 'Hello, world!'

node1.send_to_nodes(packet)
