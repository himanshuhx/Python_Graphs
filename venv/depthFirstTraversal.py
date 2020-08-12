from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSUtils(self,ele,visited):
        visited[ele] = True
        print(ele,end=' ')
        for node in self.graph[ele]:
            if not visited[node]:
                self.DFSUtils(node,visited)
    def DFS(self,source):
        visited = [False]*(len(self.graph))
        for ele in self.graph[source]:
            if not visited[ele]:
                self.DFSUtils(ele,visited)

if __name__=='__main__':
    g=Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("DFS Traversal is:")
    g.DFS(2)