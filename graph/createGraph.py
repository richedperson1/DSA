class Graph:
    def __init__(self, nVer) -> None:
        self.nVertice = nVer
        self.edgeList = [[0 for i in range(self.nVertice)]
                         for j in range(self.nVertice)]

    def containEdge(self, v1, v2):
        if self.edgeList[v1][v2]:
            return True
        return False

    def addEdge(self, v1, v2):
        self.edgeList[v1][v2] = 1
        self.edgeList[v2][v1] = 1

    def showVertice(self):
        for listing in self.edgeList:
            print(listing)

    def __str__(self):
        return str(self.edgeList)
