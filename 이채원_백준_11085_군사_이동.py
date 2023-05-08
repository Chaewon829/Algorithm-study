

import sys
from collections import deque

class Node : 
    def __init__(self,item) :
        self.item = item
        self.parent = None
        self.neighbor = []
    def connect(self, node,width) : 
        self.neighbor.append([node, width]) 

def find(nodea) : 
    if nodea.parent != nodea :
        return find(nodea.parent)
    return nodea
def union(noda,nodeb) :
           
 
def sol() : 
    p, w = map(int, sys.stdin.readline().split()) 
    c, v = map(int, sys.stdin.readline().split()) #backjoon 수도 c, Cube 수도 v
    Tree = list(Node(i) for i in range(p)) #p개의 지역(노드)
    # wlist = list(list(map(int, sys.stdin.readline().split())) for _ in range(w))
    mx = 0
    for i in range(w) :
        start, end, width = map(int, sys.stdin.readline().split())
        mx = max(width, mx)
        Tree[start].connect(node = end, width = width)
        Tree[end].connect(node = start, width = width)    
    visited = list(False for _ in range(p))
    d = deque()
    d.append([c,mx])
    visited[c] = True 
    answer = []
    while d : 
        region, width = d.pop() #stack (LIFO) 
        print("region = ",region)
        if region == v : #Cube 수도 v에 도착
            return width  
        else :
            nn = sorted(Tree[region].neighbor, key = lambda x : x[1], reverse = False)
            for r in nn :
                if visited[r[0]] == False :
                    d.append([r[0], min(width, r[1])])
        visited[region] = True
        print("deque : ", d)


print(sol())