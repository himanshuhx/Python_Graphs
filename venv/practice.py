from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices
        self.indegree=[0]*(self.V)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.indegree[v]+=1
    def topologicalSort(self):
        queue=[]
        #print(self.indegree)
        for i in range(self.V):
            if not self.indegree[i]:
                queue.append(i)
        #print(queue)
        count,topSorted=0,[]
        while queue:
            node=queue.pop(0)
            topSorted.append(node)
            for i in self.graph[node]:
                self.indegree[i]-=1
                if not self.indegree[i]:
                    queue.append(i)
            count+=1
        #print(self.indegree)
        if count!=self.V:
            print("Graph has Cycle")
        else:
            print(topSorted)


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

g.topologicalSort()


