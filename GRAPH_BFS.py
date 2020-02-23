def bfs(graph, startNode):
    __Visited, __Queue, vertexSet = [], [], []

    for _AnEdge in graph:
        for _AVertex in _AnEdge:
            if _AVertex not in vertexSet:
                vertexSet.append(_AVertex)

    def traverse_neighbors(main_node):
        if len(__Queue) == 0:
            print("Graph Traversed in order : ", __Visited)
        else:
            popped_node = __Queue.pop(len(__Queue) - 1)
            # print("node popped : " , popped_node)
            for edge in graph:
                for vertex in edge:
                    if vertex == popped_node:
                        if edge[1] in __Visited and edge[0] not in __Visited:
                            print(edge[1], "already visited")
                            __Visited.append(edge[0])
                            print("from {} visited : {} ".format(edge[1], edge[0]))
                            __Queue.append(edge[0])

                        elif edge[0] in __Visited and edge[1] not in __Visited:
                            print(edge[0], "already visited")
                            __Visited.append(edge[1])
                            print("from {} visited : {} ".format(edge[0], edge[1]))
                            __Queue.append(edge[1])
                        elif edge[0] in __Visited and edge[1] in __Visited:
                            continue
            traverse_neighbors(edge[1])

    __Visited.append(startNode)
    print("Main Node {} is visited".format(startNode))
    __Queue.append(startNode)
    traverse_neighbors(startNode)


if __name__ == "__main__":
    graph = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6)]
    bfs(graph, 4)
