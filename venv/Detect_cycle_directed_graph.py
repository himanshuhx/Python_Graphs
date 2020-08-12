from collections import defaultdict as df

class Graph:
    def __init__(self,vertices):
        self.graph=df(list)
        self.V=vertices
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def isCyclicUtils(self,vertex,visited,recur_stack):
        visited[vertex]=True
        recur_stack[vertex]=True
        for node in self.graph[vertex]:
            if not visited[vertex]:
                if self.isCyclicUtils(node,visited,recur_stack):
                    return True
            elif recur_stack[node]:
                return True
        recur_stack[vertex]=False
        return False

    def isCyclic(self):
        visited=[False]*self.V
        recur_stack=[False]*self.V
        for i in range(self.V):
            if not visited[i]:
                if self.isCyclicUtils(i,visited,recur_stack):
                    return True
        return False

if __name__=='__main__':
    g=Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("Cycle :",end=' ')
    print(g.isCyclic())