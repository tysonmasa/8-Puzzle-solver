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

def trace(state):
    print( "%i %i %i" % (state[0], state[3], state[6]))
    print( "%i %i %i" % (state[1], state[4], state[7]))
    print( "%i %i %i" % (state[2], state[5], state[8]))

def create_node(state, cost, parent_node, depth, operator):
    return Node(state, cost, parent_node, depth, operator)

def expand_node(node): # return 4 different child node
    expanded_nodes = []
    expanded_nodes.append(create_node(move.tileUp(node.state), 0, node, node.depth + 1, "Up"))
    expanded_nodes.append(create_node(move.tileDown(node.state), 0, node , node.depth + 1, "Down"))
    expanded_nodes.append(create_node(move.tileLeft(node.state), 0, node, node.depth + 1, "Left"))
    expanded_nodes.append(create_node(move.tileRight(node.state), 0, node, node.depth + 1, "Right")) # have a list of child node in 4 directions

    expanded_nodes = [node for node in expanded_nodes if node.state != None]  # keep only possible node
    return expanded_nodes

#uniform cost search
def ucs(init, goal):
    #initilize frontier with inital state of problem
    initial_node = Node(init, 0, None, 0, None)
    frontier = [initial_node]
    #initialize explored set to empty
    explored = []
    head = initial_node

    expanded_nodes = 0
    max_nodes_in_queue = 1
    while (head.state!=goal):
        #if frontier is empty, return failure
        if len(frontier) == 0:
            return 1 #"failure"
        #choose leaf node and remove from frontier
        head = frontier.pop(0)

        #if node contains goal state, return solution
        if head.state == goal:
            print(f"The depth of the goal node was", head.depth)
            continue
        #add node to explored set
        explored.append(head)
        #expand node, adding resulting nodes to frontier, if not already in frontier or expanded
        newNodes = expand_node(head)
        for item in newNodes:
            if item not in explored or item not in frontier:
                frontier.append(item)
                expanded_nodes += 1
        #sort frontier by depth
        frontier.sort(key=operator.attrgetter('depth'))

        if len(frontier) > max_nodes_in_queue:
            max_nodes_in_queue = len(frontier)

        #backtrack to get the path
    path = []
    pathLength = 0
    movesMade = []
    while(head.parent!=None):
        path.insert(0,head)
        head = head.parent
        movesMade.insert(0, head.operator)
        pathLength += 1
    print(f"Expanding state: ")
    trace(initial_node.state)
    path.reverse()
    i = pathLength - 1
    while i >= 0:
        print(f"Expanding this node with g(n) = {path[i].depth} and h(n) = 0:")
        trace(path[i].state)
        i -= 1
    print(f"Moves Made: {movesMade}")
    print(f"To solve this problem the search algorithm expanded a total of {expanded_nodes} nodes." )
    print(f"The maximum number of nodes in the queue at any one time: {max_nodes_in_queue}.")
    return path


#A* with missing tile heuristic
#heuristic
def hmissing(state, goal):
    match = 0
    for i in range(0,9):
        if state.state[i] != 0:
            if state.state[i] != goal[i]:
                match += 1
    state.heuristic=match

#function
def A_star_missing(init, goal):
    #initilize frontier with inital state of problem
    initial_node = Node(init, 0, None, 0, None)
    frontier = [initial_node]
    #initialize explored set to empty
    explored = []
    head = initial_node

    expanded_nodes = 0
    max_nodes_in_queue = 1

    while (head.state!=goal):
        #if frontier is empty, return failure
        if len(frontier) == 0:
            return 1 #"failure"
        #choose leaf node and remove from frontier
        head = frontier.pop(0)
        #if node contains goal state, return solution
        if head.state == goal:
            print(f"The depth of the goal node was", head.depth)
            exit
        #add node to explored set
        explored.append(head)
        #expand node, adding resulting nodes to frontier, if not already in frontier or expanded
        newNodes = expand_node(head)
        for item in newNodes:
            if item not in explored or item not in frontier:
                frontier.append(item)
                expanded_nodes += 1
        #sort frontier by depth + heuristic
        for item in frontier:
            hmissing(item,goal)
            item.heuristic+=item.depth
        frontier.sort(key=operator.attrgetter('heuristic'))
        #backtrack to get the path

        if len(frontier) > max_nodes_in_queue:
            max_nodes_in_queue = len(frontier)
        
    path = []
    pathLength = 0
    movesMade = []
    while(head.parent!=None):
        path.insert(0,head)
        movesMade.insert(0, head.operator)
        head = head.parent
        pathLength += 1
    print(f"Expanding state: ")
    trace(initial_node.state)
    path.reverse()
    i = pathLength - 1
    while i >= 0:
        print(f"Expanding this node with g(n) = {path[i].depth} and h(n) = {path[i].heuristic - path[i].depth}:")
        trace(path[i].state)
        i -= 1
    print(f"Moves Made: {movesMade}")
    print(f"To solve this problem the search algorithm expanded a total of {expanded_nodes} nodes." )
    print(f"The maximum number of nodes in the queue at any one time: {max_nodes_in_queue}.")
    return path

#function
def A_star_euc(init, goal):
    #initilize frontier with inital state of problem
    initial_node = Node(init, 0, None, 0, None)
    frontier = [initial_node]
    #initialize explored set to empty
    explored = []
    head = initial_node

    expanded_nodes = 0
    max_nodes_in_queue = 1

    while (head.state!=goal):
        #if frontier is empty, return failure
        if len(frontier) == 0:
            return 1 #"failure"
        #choose leaf node and remove from frontier
        head = frontier.pop(0)
        #if node contains goal state, return solution
        if head.state == goal:
            print(f"The depth of the goal node was", head.depth)
            exit
        #add node to explored set
        explored.append(head)
        #expand node, adding resulting nodes to frontier, if not already in frontier or expanded
        newNodes = expand_node(head)
        for item in newNodes:
            if item not in explored or item not in frontier:
                frontier.append(item)
                expanded_nodes += 1 
        #sort frontier by depth + heuristic
        for item in frontier:
            heuc(item, goal)  # Calculate the Euclidean distance heuristic for each node
            item.heuristic += item.depth  # Add the depth to the heuristic value
        frontier.sort(key=operator.attrgetter('heuristic'))
        #backtrack to get the path

        if len(frontier) > max_nodes_in_queue:
            max_nodes_in_queue = len(frontier)

    path = []
    movesMade = []
    pathLength = 0
    while(head.parent!=None):
        path.insert(0,head)
        movesMade.insert(0, head.operator)
        head = head.parent
        pathLength += 1
    print(f"Expanding state: ")
    trace(initial_node.state)
    path.reverse()
    i = pathLength - 1
    while i >= 0:
        print(f"Expanding this node with g(n) = {path[i].depth} and h(n) = {path[i].heuristic - path[i].depth}:")
        trace(path[i].state)
        i -= 1
    print(f"Moves Made: {movesMade}")
    print(f"To solve this problem the search algorithm expanded a total of {expanded_nodes} nodes." )
    print(f"The maximum number of nodes in the queue at any one time: {max_nodes_in_queue}.")
    return path

def goal():
    goalState = [1, 4, 7, 2, 5, 8, 3, 6, 0]
    return goalState


def main():
    userPuzzle = []

    print(f"Welcome to Group 29s 8 puzzle solver.")
    userChoice = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.\n")

    if userChoice == '1':
        print(f"Default puzzle selected.")
        # default puzzle, the very easy
        userPuzzle = [1, 4, 7, 2, 5, 0, 3, 6, 8] 
    elif userChoice == '2':
        print(f"Enter your puzzle, use a zero to represent the blank and press enter after each column.")
        #print(f"For example,\n 1 2 3\n 4 5 6\n 7 0 8\n Will be inputted as \"1 4 7\" then press enter, \"2 5 0\" then press enter, \"3 6 8\" then press enter.")

        firstRow = input("Enter the first row, use space or tabs between numbers: ")
        secondRow = input("Enter the second row, use space or tabs between numbers: ")
        thirdRow = input("Enter the third row, use space or tabs between numbers: ")

        # Uses split function to split the input into a list of strings by the spaces or tabs
        # Turns into the user input into ints
        firstRow = [int(num) for num in firstRow.split(" ")]
        secondRow = [int(num) for num in secondRow.split(" ")]
        thirdRow = [int(num) for num in thirdRow.split(" ")]

        # Our function takes it as columns 
        userPuzzle = [firstRow[0], secondRow[0], thirdRow[0], firstRow[1], secondRow[1], thirdRow[1], firstRow[2], secondRow[2], thirdRow[2]]
            
    userAlgo = input("Enter your choice of algorithm: \n1 for Uniform Cost Search\n2 for A* with the Misplaced Tile heuristic.\n3 for A* with the Euclidean distance heuristic.\nPress enter after choice of algorithm.\n")

    if userAlgo == '1':
        print(f"Uniform Cost Search selected.")
        # Do Uniform Cost Search
        movesMade = ucs(userPuzzle, goal())
        print(f"Moves made: {movesMade}")
    elif userAlgo == '2':
        print(f"A* with the Misplaced Tile heuristic selected.")
        # Do A* with Misplaced Tile heuristic
        movesMade = A_star_missing(userPuzzle, goal())
        print(f"Moves made: {movesMade}")
    elif userAlgo == '3':
        print(f"A* with the Euclidean distance heuristic selected.")
        # Do A* with Euclidean distance heuristic
        movesMade = A_star_euc(userPuzzle, goal())
        print(f"Moves made: {movesMade}")

main()
