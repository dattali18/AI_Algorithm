import heapq


def astar(graph, start, goal, heuristic):
    # Priority queue to store nodes with their respective f-cost
    priority_queue = [(0, start)]
    # Dictionary to track the g-cost (cumulative cost) to reach each node
    g_costs = {start: 0}
    # Dictionary to track the path to reach each node
    paths = {start: []}

    while priority_queue:
        # Get the node with the minimum f-cost from the priority queue
        current_f_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            # Reached the goal node
            return paths[current_node]

        for neighbor, edge_cost in graph[current_node]:
            # Calculate the g-cost (cumulative cost) to reach the neighbor node
            new_g_cost = g_costs[current_node] + edge_cost

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                # Update the g-cost and path for the neighbor node
                g_costs[neighbor] = new_g_cost
                paths[neighbor] = paths[current_node] + [neighbor]
                # Calculate the f-cost (g-cost + heuristic cost) for the neighbor node
                f_cost = new_g_cost + heuristic[neighbor]
                # Add the neighbor node to the priority queue with the f-cost
                heapq.heappush(priority_queue, (f_cost, neighbor))

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

    heuristic = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 4,
        'E': 3,
        'F': 0
    }

    path = astar(graph, start_node, goal_node, heuristic)
    print("Path:", path)


if __name__ == "__main__":
    main()
