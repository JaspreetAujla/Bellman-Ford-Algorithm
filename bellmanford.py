class Graph:

    def __init__(self, v):
        self.V = v
        self.graph = []


    def addedge(self, s, d, w):
        self.graph.append([s, d, w])


    def print_sol(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):

        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w


        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:

                print("Graph contains negative weight cycle")
                return


        self.print_sol(dist)


g = Graph(5)
g.addedge(0, 1, 2)
g.addedge(1, 2, 1)
g.addedge(2, 3, 2)
g.addedge(2, 2, 1)
g.addedge(1, 2, 2)

g.bellman_ford(0)
