def adjacency_list_to_matrix(adjacency_list):
    n = len(adjacency_list)
    matrix = [[0] * n for _ in range(n)]
    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
        print(matrix[node])
        
    return matrix