def do_bfs(graph, noOfNodes, startNode,return_distances=False):
    __Visited, __Queue, vertexSet, __distances_from_main, dicti = [], [], [], [], {}
    __FIN = []
    for _AnEdge in graph:
        for _AVertex in _AnEdge:
            if _AVertex not in vertexSet:
                vertexSet.append(_AVertex)

    def traverse_neighbors(main_node, j, k):
        i = j
        k = k
        m = len(__Visited)
        if len(__Queue) == 0:
            print("Graph Traversed in order : ", __Visited)
        else:
            popped_node = __Queue.pop(len(__Queue) - 1)
            # print("node popped : " , popped_node)
            for edge in graph:
                for vertex in edge:
                    if vertex == popped_node:
                        if edge[1] in __Visited and edge[0] not in __Visited:
                            __Visited.append(edge[0])
                            print("from {} visited : {} ".format(edge[1], edge[0]))
                            __Queue.append(edge[0])

                        elif edge[0] in __Visited and edge[1] not in __Visited:
                            __Visited.append(edge[1])
                            print("from {} visited : {} ".format(edge[0], edge[1]))
                            __Queue.append(edge[1])
                        elif edge[0] in __Visited and edge[1] in __Visited:
                            continue
            __distances_from_main.append(__Visited[k:len(__Visited)])
            k = len(__Visited)
            __Queue.sort(reverse=True)  # to start traversing from small number neighbors
            dicti[i + 1] = __distances_from_main[i]
            traverse_neighbors(edge[1], i + 1, k)  # passing shit value

    __Visited.append(startNode)
    print("Main Node {} is visited".format(startNode))
    __Queue.append(startNode)
    traverse_neighbors(startNode, 0, 0)
    if return_distances:
        for i in range(1, noOfNodes + 1):
            if i not in dicti.keys():
                __FIN.append(-1)
                continue
            for nodeD in dicti[i]:
                if nodeD == 1:
                    continue
                else:
                    __FIN.append(i * 6)

        return __FIN
    else:
        print("distances : ", dicti)


def bfs(no_of_nodes, no_of_edges, edge_pair, startNode):
    graph_ = []
    N = no_of_nodes
    M = no_of_edges
    for edge in edge_pair:
        graph_.append((edge[0], edge[1]))
    distances = do_bfs(graph_, N, startNode, return_distances=True)
    return distances


# graph = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6)]
# graph = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 1), (3, 2)]
if __name__ == "__main__":
    edge_list = [[1, 2], [1, 3]]
    distances_of_nodes = bfs(4, 2, edge_list , 1)
    print(distances_of_nodes)
