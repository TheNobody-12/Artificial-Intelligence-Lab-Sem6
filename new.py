class Node:
    def _init_(self, name, ):
        self.name = name
        self.adj = []
    
    def addPath(self, adjNode, cost):
        self.adj.append((adjNode, cost))
    
    def getAdj(self):
        return self.adj


class priorityQueue:
    def _init_(self):
        self.queue = []
    
    def add(self, child, parent, cost):
        index = 0 
        for i in self.queue:
            if i[2] < cost:
                index+=1
            if i[0] == child:
                if cost > i[2]:
                    return
                else:
                    self.queue.remove(i)
                    break
        self.queue.insert(index, (child, parent, cost))
    
    def pop(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            print("Queue is Empty")
            return False
    
    def isEmpty(self):
        return len(self.queue) == 0


def check(ele, List, index):
    for i in List:
        if i[index] == ele:
            return True
    return False

def Astar(start, goal):
    queue = priorityQueue()
    queue.add(start, None, 0)
    visited = []
    while not queue.isEmpty():
        current = queue.pop()
        if current[0] == goal:
            path = []
            while current[1] != None:
                path.append(current[0])
                current = current[1]
            path.append(start)
            path.reverse()
            return path
        if not check(current[0], visited, 0):
            visited.append(current)
            for i in current[0].adj:
                queue.add(i[0], current, i[1] + current[2])
    return False

S = Node("S")
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G1 = Node("G1")
G2 = Node("G2")
G3 = Node("G3")

S.addPath(A,5)
S.addPath(B,9)
S.addPath(D,6)

A.addPath(B,3)
A.addPath(G1,9)

B.addPath(A,2)
B.addPath(C,1)

C.addPath(S,6)
C.addPath(G2,5)
C.addPath(F,7)

D.addPath(C,2)
D.addPath(E,2)

E.addPath(G3, 7)

F.addPath(D, 2)
F.addPath(G3,8)

Start = S
Goal = G2

path = Astar((Start, None, 0), Goal)