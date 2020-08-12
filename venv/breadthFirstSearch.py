from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,source):
        visited=[False]*(len(self.graph))
        queue=[]
        queue.append(source)
        visited[source]=True
        while queue:
            node=queue.pop(0)
            print(node,end=' ')
            for ele in self.graph[node]:
                if not visited[ele]:
                    queue.append(ele)
                    visited[ele]=True
if __name__=='__main__':
    g=Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("BFS Traversal is:")
    g.BFS(2)
