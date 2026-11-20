def n_queens(n: int) -> int:
    """Compute number of ways to place n queens on a n x n board via backtracking."""
    num_ways = 0

    stack = [(0, [False] * n, [False] * ((2 * n) - 1), [False] * ((2 * n) - 1))]
    while stack:
        y, cols, diags, rev_diags = stack.pop()
        
        if y == n:
            num_ways += 1
        else:
            for x in range(n):
                if not cols[x] and not diags[x + y] and not rev_diags[x - y + n - 1]:
                    cols[x] = True
                    diags[x + y] = True
                    rev_diags[x - y + n - 1] = True
                    
                    stack.append((y + 1, list(cols), list(diags), list(rev_diags)))
                    
                    cols[x] = False
                    diags[x + y] = False
                    rev_diags[x - y + n - 1] = False

    return num_ways


assert n_queens(8) == 92
