# Water Jug problem

MaxA = 5
MaxB = 4

def getChild(node):
    a = node[0]
    b = node[1]
    # print(a, node, node[0], node[1])

    child = []
    # Empty:
    if a != 0:
        child.append([0,b])
        # transfer A to B
        if b < MaxB:
            child.append([max(0, a+b-MaxB), min(MaxB, a+b)])
    if b != 0:
        child.append([a,0])
        # transfer B to A
        if a < MaxA:
            child.append([min(MaxA, a+b), max(0, a+b-MaxA)])
    
    # Fill:
    if a < MaxA:
        child.append([MaxA, b])
    if b < MaxB:
        child.append([a, MaxB])
    
    return child


def bfs(start, goal):
    current = start
    q = [start]
    visited = []
    parent = []

    while (len(q) != 0) and current != goal:
        q.pop(0)
        visited.append(current)
        # print(":  child: ",getChild(current), "\n:  current: ",current, ":  queue: ", q)
        for i in getChild(current):
            q.append(i)
        current = q[0]
    
    path = [goal]
    
    lv = goal
    for i in visited[::-1]:
        if lv in getChild(i):
            path.append(i)
            lv = i
        else:
            continue
    print("Traversal:",(visited))
    print("Path:",(path[::-1]))

bfs(start=[0,0],goal=[2,0])