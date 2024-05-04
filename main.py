import operator

#node
class Node:
    def init(self, state, cost, parent_node, depth, operator):
        self.state = state # showing the current state, would be something like (1,2,3,4,5,6,7,8,*)
        self.cost = cost # showing the cost to reach this node
        self.parent = parent_node # showing its parent node
        self.depth = depth # showing the depth of this node
        self.operator = operator # showing the operator that create this node

def expand_node(node):
    #return list of expanded nodes
    pass

#uniform cost search
def ucs(init, goal):
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


#A* with Euclidean distance heuristic
#heuristic
def heuc(state, goal):
    match = 0
    for i in range(0,9):
        if state.state[i] != goal[i]:
            match += 1
    state.heuristic=match

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


#Main
def main():
    print("whats up")

main()