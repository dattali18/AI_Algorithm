def id_dfs(graph, start, target, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        path = []  # Initialize an empty list to store the path
        if dfs(graph, start, target, depth, visited, path):
            return path  # Return the path if the target is found
    return None  # Return None if the target is not found within the specified depth


def dfs(graph, node, target, depth, visited, path):
    if depth == 0 and node == target:
        path.append(node)  # Add the target node to the path
        return True
    if depth > 0:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                path.append(node)  # Add the current node to the path
                if dfs(graph, neighbor, target, depth - 1, visited, path):
                    return True
                path.pop()
                # Remove the current node from the path if the search in this direction didn't find the target
    return False


def main():
    graph = {
        'A': ['B', 'H'],
        'B': ['G', 'C'],
        'C': ['D', 'F'],
        'D': ['E'],
        'E': [],
        'F': [],
        'H': ['I'],
        'I': ['J', 'K'],
        'J': [],
        'K': []
    }

    start_node = 'A'
    target_node = 'G'
    max_depth = 3

    path = id_dfs(graph, start_node, target_node, max_depth)
    if path:
        print("Target node found. Path:", path)
    else:
        print("Target node not found within the specified depth.")


if __name__ == "__main__":
    main()
