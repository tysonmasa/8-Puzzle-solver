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

def expand_node(node):
    #return list of expanded nodes
    pass

#A* with Euclidean distance heuristic
#heuristic
def i_to_position(i);
    return(i//3, i%3)

def heuc(state, goal):
    match = 0
    for i in range(9):
        if state.state[i] != goal[i] and state.state[i] != 0:
            state_pos = i_to_position(i)
            goal_pos = i_to_position(goal.index(state.state[i]))
            match += ((state_pos[0] - goal_pos[0]) ** 2 + (state_pos[1] - goal_pos[1]) ** 2) ** 0.5
    state.heuristic = match

#function
def A_star_euc(init, goal):
    #initilize frontier with inital state of problem
    initial_node = Node(init, None, None, 0, 0)
    frontier = [initial_node]
    #initialize explored set to empty
    explored = []
    head = None
    while (head.state!=goal):
        #if frontier is empty, return failure
        if len(frontier) == 0:
            return 1 #"failure"
        #choose leaf node and remove from frontier
        head = frontier.pop(0)
        #if node contains goal state, return solution
        if head.state == goal:
            exit
            #add node to explored set
        explored.append(head)
        #expand node, adding resulting nodes to frontier, if not already in frontier or expanded
        newNodes = expand_node(head)
        for item in newNodes:
            if item not in explored or item not in frontier:
                frontier.append(item)
        #sort frontier by depth + heuristic
        for item in frontier:
            hmissing(item,goal)
            item.heuristic+=item.depth
        frontier.sort(key=operator.attrgetter('heuristic'))
        #backtrack to get the path
    path = []
    while(head.parent!=None):
        path.insert(0,head.operator)
        head = head.parent
    return path