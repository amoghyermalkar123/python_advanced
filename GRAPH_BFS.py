def do_bfs(graph, start_node):
    visited, queue = [], []
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        popped_node = queue.pop(0)
        for neighbor in graph[popped_node]:
            if neighbor not in visited:
                print("from node {} visited node {}".format(popped_node, neighbor))
                visited.append(neighbor)
                queue.append(neighbor)


def bfs(no_of_nodes, no_of_edges, edge_pair, startNode):
    graph = {}
    _all_nodes, _distances = [], []
    for v1, v2 in edge_pair:  # BUILDING ALL NODES LIST
        if v1 not in _all_nodes:
            _all_nodes.append(v1)
        elif v2 not in _all_nodes:
            _all_nodes.append(v2)
        else:
            continue

    for node in range(1, no_of_nodes + 1):
        if node not in _all_nodes:
            _all_nodes.append(node)

    _all_nodes.sort()
    if _all_nodes[0] == 0:
        _all_nodes.pop(0)

    # FINAL ALL NODES LIST READY

    def get_ngh(_node, _edge_list):
        neigh = []
        for v1, v2 in _edge_list:
            if v1 == _node and v2 not in neigh:
                neigh.append(v2)
            elif v2 == _node and v1 not in neigh:
                neigh.append(v1)
            else:
                continue
        return neigh

    for node in _all_nodes:
        graph[node] = get_ngh(node, edge_pair)
        # print("Node is {} and its neighbors are {}".format(node, graph[node]))

    print("All nodes list : ", _all_nodes)
    print("The starting node is {}, the BFS will start from this node".format(startNode))
    print("BFS starting...")

    do_bfs(graph, startNode)


if __name__ == "__main__":
    edge_list = [[1, 2], [1, 3], [2, 1], [6, 3], [1, 4], [2, 5], [5, 6], [6, 7], [5, 6], [3, 6]]
    bfs(7, 10, edge_list, 1)


"""
    Some pre-prepared graphs :

    edge_list = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [5, 8]]
    distance = bfs(9, 7, edge_list, 1)


    edge_list = [[3, 1], [10, 1], [10, 1], [3, 1], [1, 8], [5, 2]]
    distance = bfs(10, 6, edge_list, 3)

    edge_list = [[3, 1], [3, 4], [10, 1], [10, 4], [7, 8], [4, 7], [10, 7]]
    distance = bfs(10, 7, edge_list, 2)



"""