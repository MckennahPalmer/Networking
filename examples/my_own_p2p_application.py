#######################################################################################################################
# Author: Mckennah Palmer                                                                                           #
# Application: Marco Polo Finder App (The start of it)                                                              #                                                                                                #
#######################################################################################################################

import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located if that is needed.

from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode

node_1 = MyOwnPeer2PeerNode("127.0.0.1", 8001, 1)
node_2 = MyOwnPeer2PeerNode("127.0.0.1", 8002, 2)
node_3 = MyOwnPeer2PeerNode("127.0.0.1", 8003, 3)

time.sleep(1)

#Open the nodes
node_1.start()
node_2.start()
node_3.start()

time.sleep(1)

debug = False
node_1.debug = debug
node_2.debug = debug
node_3.debug = debug

#Connect the nodes
node_1.connect_with_node('127.0.0.1', 8002)
node_2.connect_with_node('127.0.0.1', 8003)
node_3.connect_with_node('127.0.0.1', 8001)

time.sleep(2)

#Node one sends Marco to other nodes first
node_1.send_to_nodes("message: Marco!")

time.sleep(2)

#Node one stop sending message
print("node 1 is stopping..")
node_1.stop()

time.sleep(20)

#Nodes 2 and 3 both send Polo back to the other nodes
node_2.send_to_nodes("message: Polo!")
node_2.send_to_nodes("message: Polo!")
node_2.send_to_nodes("message: Polo!")
node_3.send_to_nodes("message: Polo!")
node_3.send_to_nodes("message: Polo!")
node_3.send_to_nodes("message: Polo!")

time.sleep(10)

time.sleep(5)

#Nodes 2 and 3 stop sending the message
node_1.stop()
node_2.stop()
node_3.stop()

#End of Program
print('end test')
