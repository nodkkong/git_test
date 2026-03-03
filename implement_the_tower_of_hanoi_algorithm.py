def hanoi_solver(n):
    rod_1 = list(range(n, 0, -1))
    rod_2 = []
    rod_3 = []
    moves = []

    def move(n, source, target, auxiliary):
        if n == 0:
            return
        
        move(n-1, source, auxiliary, target)
        largest = source.pop(-1)
        target.append(largest)
        moves.append(f'{rod_1} {rod_2} {rod_3}')
        move(n-1, auxiliary, target, source)

        

    moves.append(f'{rod_1} {rod_2} {rod_3}')
    move(n, rod_1, rod_3, rod_2)
    return '\n'.join(moves)