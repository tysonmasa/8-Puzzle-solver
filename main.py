import sys
from pythonds.basic.stack import Stack
from operator import attrgetter


class Node:
    def __init__(self, state, cost, parent_node, depth, operator):
        self.state = state # showing the current state, would be something like (1,2,3,4,5,6,7,8,*)
        self.cost = cost # showing the cost to reach this node
        self.parent = parent_node # showing its parent node
        self.depth = depth # showing the depth of this node
        self.operator = operator # showing the operator that create this node
        

        self.heuristic=None # initialize the heuristic to be none

def display_board(state):
    print( "State:")
    print( "%i %i %i" % (state[0], state[3], state[6]))
    print( "%i %i %i" % (state[1], state[4], state[7]))
    print( "%i %i %i" % (state[2], state[5], state[8]))

def create_node(state, cost, parent_node, depth, operator):
    return Node(state, cost, parent_node, depth, operator)

def expand_node(node): # return 4 differnet child node
    expanded_nodes = []
    expanded_nodes.append(create_node(move_up(node.state), 0, node, node.depth + 1, "u"))
    expanded_nodes.append(create_node(move_down(node.state), 0, node , node.depth + 1, "d"))
    expanded_nodes.append(create_node(move_left(node.state), 0, node, node.depth + 1, "l"))
    expanded_nodes.append(create_node(move_right(node.state), 0, node, node.depth + 1, "r")) # have a list of child node in 4 directions

    expanded_nodes = [node for node in expanded_nodes if node.state != None]  # keep only possible node
    return expanded_nodes

