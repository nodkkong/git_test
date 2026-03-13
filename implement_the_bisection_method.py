def square_root_bisection(n, tolerance=1e-7, max_num=100):
    if n < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif n == 0 or n == 1:
        print(f'The square root of {n} is {n}')
        return n

    low = 0
    high = max(1, n)
    root = None

    for num in range(max_num):
        mid = (low + high) / 2
        if abs(mid - (n / mid)) <= tolerance:
            root = mid
            break

        elif mid * mid < n:
            low = mid
        
        else:
            high = mid

    if root is not None:
        print(f'The square root of {n} is approximately {root}')
        return root

    if root is None:
        print(f'Failed to converge within {max_num} iterations')
        return None