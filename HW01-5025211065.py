import heapq

def dijkstra(graph, start, end):
    # Create a dictionary to store the distance from the start vertex to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Create a priority queue to store vertices with their distances
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If we have already visited this vertex, continue to the next one
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If this path is shorter than the currently recorded distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the shortest path
    path = []
    current_vertex = end
    while current_vertex != start:
        path.append(current_vertex)
        for neighbor, weight in graph[current_vertex].items():
            if distances[current_vertex] == distances[neighbor] + weight:
                current_vertex = neighbor
                break
    path.append(start)
    path.reverse()

    # Calculate the total weight of the shortest path
    total_weight = distances[end]

    return path, total_weight

# Define the graph
graph = {
    'A': {'B': 1, 'C': 3, 'D': 5},
    'B': {'A': 1, 'E': 7, 'F': 4},
    'C': {'A': 3, 'F': 1},
    'D': {'A': 5, 'G': 2},
    'E': {'B': 7, 'G': 1, 'H': 6},
    'F': {'B': 4, 'C': 1, 'G': 2},
    'G': {'D': 2, 'E': 1, 'F': 2, 'J': 4, 'L': 1},
    'H': {'E': 6, 'I': 2, 'M': 4},
    'I': {'H': 2, 'J': 1, 'K': 1, 'M': 7},
    'J': {'F': 6, 'G': 4, 'I': 1},
    'K': {'I': 1, 'L': 4},
    'L': {'G': 1, 'M': 3},
    'M': {'H': 4, 'I': 7, 'L': 3}
}

# Define the source and target vertices
vs = 'A'
Vt = 'M'

# Find the shortest path and total weight
shortest_path, total_weight = dijkstra(graph, vs, Vt)

# Print the results
print(f"Shortest Path from {vs} to {Vt}: {shortest_path}")
print(f"Total Weight: {total_weight}")