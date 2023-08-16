from collections import deque


def bfs(graph, start):
    visited = set()  # Set to track visited nodes
    queue = deque([start])  # Queue to keep track of nodes to visit

    while queue:
        node = queue.popleft()  # Get the next node from the queue

        if node not in visited:
            visited.add(node)  # Mark node as visited
            print(node)  # Process the node (print it in this case)

            # Add unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    bfs(graph, 'A')


if __name__ == "__main__":
    main()
