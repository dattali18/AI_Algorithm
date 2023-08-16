import heapq


def ucs(graph, start, goal):
    # Priority queue to store nodes with their respective path cost
    priority_queue = [(0, start)]
    # Dictionary to track the cumulative cost to reach each node
    costs = {start: 0}
    # Dictionary to track the path to reach each node
    paths = {start: []}

    while priority_queue:
        # Get the node with the minimum cost from the priority queue
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            # Reached the goal node
            return paths[current_node]

        for neighbor, edge_cost in graph[current_node]:
            # Calculate the new cost to reach the neighbor node
            new_cost = current_cost + edge_cost

            if neighbor not in costs or new_cost < costs[neighbor]:
                # Update the cost and path for the neighbor node
                costs[neighbor] = new_cost
                paths[neighbor] = paths[current_node] + [neighbor]
                # Add the neighbor node to the priority queue with the new cost
                heapq.heappush(priority_queue, (new_cost, neighbor))

    # No path found from start to goal
    return None


def main():
    graph = {
        'A': [('B', 5), ('C', 3)],
        'B': [('D', 2)],
        'C': [('D', 6), ('E', 4)],
        'D': [('F', 1)],
        'E': [('F', 3)],
        'F': []
    }

    start_node = 'A'
    goal_node = 'F'

    path = ucs(graph, start_node, goal_node)
    print("Path:", path)


if __name__ == "__main__":
    main()
