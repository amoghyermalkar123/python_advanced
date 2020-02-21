def bfs(graph, startNode):
    __Visited = []
    __Queue = []
    
    VertexSet = []
    for _AnEdge in graph:
        for _AVertex in _AnEdge:
            if _AVertex not in VertexSet:
                VertexSet.append(_AVertex)
    
    def traverse_neighbors(main_node):
        if len(__Queue) == 0:
            print("Graph Traversed in order : ", __Visited)
        else :
            popped_node = __Queue.pop(len(__Queue) - 1)
            # print("node popped : " , popped_node)
            for edge in graph:
                for vertex in edge:
                    if vertex == popped_node:
                        if edge[1] in __Visited:
                            continue
                
                        else:
                            __Visited.append(edge[1])
                            print("node visited : ", edge[1])
                            __Queue.append(edge[1])
            traverse_neighbors(edge[1])

    __Visited.append(startNode)
    print("Main Node {} is visited".format(startNode))
    __Queue.append(startNode)
    traverse_neighbors(startNode)


# graph = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6)]
graph = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 1), (3, 2)]
bfs(graph, 0)
