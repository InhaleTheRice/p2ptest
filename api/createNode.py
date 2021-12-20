import sys
import time
from .TangerineNode import TangerineNode

def createNode(host, port):
	node = TangerineNode(host, port)
	time.sleep(1)

	node.start()
	time.sleep(1)

	return node
