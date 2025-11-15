class UDGraph:
    def __init__(self):
        self.adj_list = {}   # { vertex: [outgoing neighbours] }

    def addVertex(self, vertex):
        """
        Add a new vertex to the graph
        Represents adding users to the app
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def addEdge(self, from_vertex, to_vertex):
        """
        Add a new directed edge
        Represents following feature
        """

        # Check and see if both the vertices exists or not
        if from_vertex not in self.adj_list:
            raise ValueError(f"Vertex {from_vertex} does not exist.")

        if to_vertex not in self.adj_list:
            raise ValueError(f"Vertex {to_vertex} does not exist.")

        if to_vertex not in self.adj_list[from_vertex]:
            self.adj_list[from_vertex].append(to_vertex)

    def listOutgoingAdjacentVertex(self, vertex):
        """
        List outgoing adjacent vertex
        Represents who is following who
        """
        return self.adj_list.get(vertex, [])


    def listIncomingAdjacent(self, vertex):
        """List incoming edges (Represents followers)"""
        incoming = []

        for v, neighbours in self.adj_list.items():
            if vertex in neighbours:
                incoming.append(v)
        return incoming

    def removeEdge(self, from_vertex, to_vertex):
        """Remove edge from the graph"""
        if from_vertex in self.adj_list and to_vertex in self.adj_list[from_vertex]:
            self.adj_list[from_vertex].remove(to_vertex)

    def getAllVertices(self):
        """Retrieve all the vertices"""
        return list(self.adj_list.keys())

    def printGraph(self):
        """Display the graph network"""
        for vertex, neighbours in self.adj_list.items():
            print(f"{vertex} -> {neighbours}")