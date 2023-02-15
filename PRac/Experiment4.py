class Node:
    def _init_(self, data, parent):            
        self.data = data
        self.parent = parent
        self.child = []
    
    def setChild(self, child):
        self.child = child
    
    def getChildren(self):
        return self.child
    
    def getAdjacent(self):
        temp = self.child
        if self.parent != None:
            temp.append(self.parent)
        return temp
    

MaxA = 5
MaxB = 4

def getChild(parent, stack):
    a = parent.data[0]
    b = parent.data[1]

    child = []
    # Empty:
    if a != 0:
        if [0,b] not in stack:
            temp = Node([0,b], parent)
            child.append(temp)
        # transfer A to B
        if b < MaxB:
            if [max(0, a+b-MaxB), min(MaxB, a+b)] not in stack:
                temp = Node([max(0, a+b-MaxB), min(MaxB, a+b)], parent)
                child.append(temp)
    if b != 0:
        if [a,0] not in stack:
            temp = Node([a,0], parent)
            child.append(temp)
        # transfer B to A
        if a < MaxA:
            if [min(MaxA, a+b), max(0, a+b-MaxA)] not in stack:
                temp = Node([min(MaxA, a+b), max(0, a+b-MaxA)], parent)
                child.append(temp)
    
    # Fill:
    if a < MaxA:
        if [MaxA,b] not in stack:
            temp = Node([MaxA, b], parent)
            child.append(temp)
    if b < MaxB:
        if [a, MaxB] not in stack:
            temp = Node([a, MaxB], parent)
            child.append(temp)
    
    return child

def searchSpaceBFS(start, goal):
    root = Node(start, None)
    temp = root

    current = start
    q = [start]
    visited = []

    while (len(q) != 0) and current != goal:
        q.pop(0)
        visited.append(current)

        temp.setChild(getChild(temp, visited))

        for i in temp.getChildren():
            q.append(i)

        current = q[0].data
        temp = q[0]

    return [root, temp]


def intersect(q1,q2):
    for i in q1:
        if i in q2:
            return [True,i]
    return [False, 0]

def show(q):
    for i in q:
        print(i.data, end=' ')

def biDirectionalSearch(start, goal):
    open1 = [start, ]
    open2 = [goal, ]
    closed1 = []
    closed2 = []
    n1 = start
    n2 = goal

    while not intersect(open1,open2)[0]:

        # bfs step for start side
        for i in n1.getChildren():
            open1.append(i)
        closed1.append(open1.pop(0))
        n1 = open1[0]

        # bfs step for goal side
        for i in n2.getAdjacent():
            if i not in closed2:
                open2.append(i)
        closed2.append(open2.pop(0))
        n2 = open2[0]
    
                                                                                                                                                                                                                                                                                                                                                                                        
    joint = intersect(open1, open2)[1]
    path = closed1
    path.append(joint)
    [path.append(i) for i in closed2[::-1]]

    print("Traversal: ")
    print(show(path))

    current = goal
    for i in path[::-1]:
        if i == goal:
            continue
        if i not in current.getAdjacent():
            path.remove(i)
        else:
            current = i
    return path

def printPath(path):
    for i in path[:-1]:
        print(i.data, end=" -> ")
    print(path[-1].data)

start, goal = searchSpaceBFS( [0,0], [2,0],)
path = biDirectionalSearch(start, goal)
printPath(path)