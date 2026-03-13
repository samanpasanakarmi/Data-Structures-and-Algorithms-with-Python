def dijkstra_shortest_path(source_vertex, destination_vertex, graph):
   

    def get_weight(edge):
       
        for name in ["weight", "_weight", "value", "_value", "_element", "element"]:
            if hasattr(edge, name):
                attr = getattr(edge, name)
                return attr() if callable(attr) else attr

      
        if hasattr(edge, "__dict__"):
            for v in edge.__dict__.values():
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    return v

        return None

    vertices = graph.get_vertices()
    unvisited = set(vertices)

    distances = {}
    previous = {}

    for v in vertices:
        distances[v] = float('inf')
        previous[v] = None

    distances[source_vertex] = 0

    while unvisited:
        current = min(unvisited, key=lambda v: distances[v])

        if distances[current] == float('inf'):
            break

        unvisited.remove(current)

        if current == destination_vertex:
            break

        for neighbour in graph.get_adjacent_vertices(current):
            if neighbour in unvisited:
                edge = graph.get_edge(current, neighbour)
                weight = get_weight(edge)
                new_distance = distances[current] + weight

                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    previous[neighbour] = current

    if distances[destination_vertex] == float('inf'):
        return (float('inf'), [])

    path = []
    current = destination_vertex

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return (distances[destination_vertex], path)