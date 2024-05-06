import move
import sys
import operator
from operator import attrgetter

#node
class Node:
    def __init__(self, state, cost, parent_node, depth, operator):
        self.state = state # showing the current state, would be something like (1,2,3,4,5,6,7,8,*)
        self.cost = cost # showing the cost to reach this node
        self.parent = parent_node # showing its parent node
        self.depth = depth # showing the depth of this node
        self.operator = operator # showing the operator that create this node

        self.heuristic=None # initialize the heuristic to be none

#A* with Euclidean distance heuristic
#heuristic
def i_to_position(i):
    return(i//3, i%3)

def heuc(state, goal):
    match = 0
    for i in range(9):
        if state.state[i] != goal[i] and state.state[i] != 0:
            state_pos = i_to_position(i)
            goal_pos = i_to_position(goal.index(state.state[i]))
            match += ((state_pos[0] - goal_pos[0]) ** 2 + (state_pos[1] - goal_pos[1]) ** 2) ** 0.5
    state.heuristic = match

def display_board(state):
    print( "State:")
    print( "%i %i %i" % (state[0], state[3], state[6]))
    print( "%i %i %i" % (state[1], state[4], state[7]))
    print( "%i %i %i" % (state[2], state[5], state[8]))

def create_node(state, cost, parent_node, depth, operator):
    return Node(state, cost, parent_node, depth, operator)

def expand_node(node): # return 4 different child node
    expanded_nodes = []
    expanded_nodes.append(create_node(move.tileUp(node.state), 0, node, node.depth + 1, "u"))
    expanded_nodes.append(create_node(move.tileDown(node.state), 0, node , node.depth + 1, "d"))
    expanded_nodes.append(create_node(move.tileLeft(node.state), 0, node, node.depth + 1, "l"))
    expanded_nodes.append(create_node(move.tileRight(node.state), 0, node, node.depth + 1, "r")) # have a list of child node in 4 directions

    expanded_nodes = [node for node in expanded_nodes if node.state != None]  # keep only possible node
    return expanded_nodes

#uniform cost search
def ucs(init, goal):
    #initilize frontier with inital state of problem
    initial_node = Node(init, None, None, 0, 0)
    frontier = [initial_node]
    #initialize explored set to empty
    explored = []
    head = initial_node
    while (head.state!=goal):
        print("frontier")
        #if frontier is empty, return failure
        if len(frontier) == 0:
            return 1 #"failure"
        #choose leaf node and remove from frontier
        print(head.state)
        head = frontier.pop(0)
        print(head.state)
        #if node contains goal state, return solution
        if head.state == goal:
            continue
        #add node to explored set
        explored.append(head)
        #expand node, adding resulting nodes to frontier, if not already in frontier or expanded
        newNodes = expand_node(head)
        for item in newNodes:
            if item not in explored or item not in frontier:
                frontier.append(item)
        #sort frontier by depth
        frontier.sort(key=operator.attrgetter('depth'))
        #backtrack to get the path
    path = []
    while(head.parent!=None):
        path.insert(0,head.operator)
        head = head.parent
    return path


#A* with missing tile heuristic
#heuristic
def hmissing(state, goal):
    match = 0
    for i in range(0,9):
        if state.state[i] != goal[i]:
            match += 1
    state.heuristic=match

#function
def A_star_missing(init, goal):
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

def goal():
    goalState = [1, 4, 7, 2, 5, 8, 3, 6, 0]
    return goalState


def main():
    print(f"Welcome to Group 29s 8 puzzle solver.")
    userChoice = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.\n")

    if userChoice == '1':
        print(f"Default puzzle selected.")
        # default puzzle, the very easy
        userPuzzle = [1, 4, 7, 2, 5, 0, 3, 6, 8] 
    elif userChoice == '2':
        print(f"Enter your puzzle, use a zero to represent the blank and press enter after each column.")
        firstRow = input("Enter the first column, use space or tabs between numbers: ")
        secondRow = input("Enter the second column, use space or tabs between numbers: ")
        thirdRow = input("Enter the third column, use space or tabs between numbers: ")

        # Uses split function to split the input into a list of strings by the spaces or tabs
        firstRow = firstRow.split(" ")
        secondRow = secondRow.split(" ")
        thirdRow = thirdRow.split(" ")

        # Combines them into list
        userPuzzle = firstRow, secondRow, thirdRow

    
    userAlgo = input("Enter your choice of algorithm: \n1 for Uniform Cost Search\n2 for A* with the Misplaced Tile heuristic.\n3 for A* with the Euclidean distance heuristic.\nPress enter after choice of algorithm.\n")

    if userAlgo == '1':
        print(f"Uniform Cost Search selected.")
        # Do Uniform Cost Search
        finished = ucs(userPuzzle, goal())
        print(finished)
    elif userAlgo == '3':
        print(f"A* with the Misplaced Tile heuristic selected.")
        # Do A* with Misplaced Tile heuristic
    elif userAlgo == '3':
        print(f"A* with the Euclidean distance heuristic selected.")
        # Do A* with Euclidean distance heuristic

main()
