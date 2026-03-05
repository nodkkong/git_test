def dfs(und_adj_matrix, node_label):
    stack = [node_label]
    visited = []

    while stack:
        current = stack.pop(-1)
        if current not in visited:
            visited.append(current)
            for node_no, weight in enumerate(und_adj_matrix[current]):
                if weight == 1:
                    stack.append(node_no)
    return visited