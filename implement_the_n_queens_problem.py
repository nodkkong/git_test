def dfs_n_queens(n):
    if n < 1:
        return []
    stack = [[]]
    solutions = []

    while stack:
        current = stack.pop(-1)
        if len(current) == n:
            solutions.append(current)
        else:
            for col in range(n):
                is_valid = True
                for row in range(len(current)):
                    if current[row] == col or abs(current[row] - col) == abs(row - len(current)):
                        is_valid = False
                        break
                if is_valid:
                    stack.append(current + [col])
    solutions = solutions[::-1]
    return solutions

print(dfs_n_queens(4))