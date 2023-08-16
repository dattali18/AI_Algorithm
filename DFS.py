def dfs(graph, start):
    visited = set()  # Set to track visited nodes
    stack = [start]  # Stack to keep track of nodes to visit

    while stack:
        node = stack.pop()  # Get the next node from the stack

        if node not in visited:
            visited.add(node)  # Mark node as visited
            print(node)  # Process the node (print it in this case)

            # Add unvisited neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    dfs(graph, 'A')


if __name__ == "__main__":
    main()