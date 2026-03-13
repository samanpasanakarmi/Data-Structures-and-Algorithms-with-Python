def BFS(graph, start):
    

    visited = {start: None}
    queue = [start]

    while queue:
        u = queue.pop(0)

        for v in graph.get_adjacent_vertices(u):
            if v not in visited:
                visited[v] = u
                queue.append(v)

    return visited