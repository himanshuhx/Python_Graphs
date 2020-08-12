from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCyclicUtils(self,node,visited,parent):
        visited[node]=True
        for ele in self.graph[node]:
            if not visited[ele]:
                if self.isCyclicUtils(ele,visited,node):
                    return True
                elif parent!=node: #if visited[node]==True and not parent of current node
                    return True    #there is a cycle
        return False

    def isCyclic(self):
        visited=[False]*(len(self.graph))
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtils(node,visited,-1):
                    return True
            return False

if __name__=='__main__':
    g=Graph(5) #taking vertices count as input for simplicity
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    print("Cycle :",end=' ')
    print(g.isCyclic())