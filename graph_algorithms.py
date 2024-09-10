from collections import deque


def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    steps = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            steps.append(node)

            for neighbor in graph.get_neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)

    return steps


def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    steps = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            steps.append(node)

            for neighbor in graph.get_neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)

    return steps