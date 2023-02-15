# Name: Sarthak Kapaliya
# Roll No: 20BCP072
# Batch: CSE Div G2
#  Water Jug problem
MaxA = 5
MaxB = 4

def getChild(node):
    a = node[0]
    b = node[1]
    child = []
    # Empty:
    if a != 0:
        child.append([0, b])
        # transfer A to B
        if b < MaxB:
            child.append([max(0, a+b-MaxB), min(MaxB, a+b)])
    if b != 0:
        child.append([a, 0])
        # transfer B to A
        if a < MaxA:
            child.append([min(MaxA, a+b), max(0, a+b-MaxA)])

    # Fill:
    if a < MaxA:
        child.append([MaxA, b])
    if b < MaxB:
        child.append([a, MaxB])
    return child


def dfs(start, goal, stack):
    child = getChild(start)
    stack.append(start)
    if start == goal:
        return [stack]

    for i in child:
        if i not in stack:
            leaf = dfs(i, goal, stack)
            if leaf != None:
                if goal in leaf:
                    print(start)
                    return leaf.append(start)
    
    return [stack]

start = [0,0]
goal = [2,0]

path = dfs(start, goal, [])
print("path: ", path[::-1])