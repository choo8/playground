def iteration(n: int) -> list[list[int]]:
    """Iterative method of generating subsets of a set of n elements via depth first search."""
    results = []

    stack = [(1, [])]
    while stack:
        k, subset = stack.pop()

        if k == n + 1:
            results.append(list(subset))
        else:
            stack.append((k + 1, subset + [k]))
            stack.append((k + 1, subset))

    return results


def recursion(n: int) -> list[list[int]]:
    """Recursive method of generating subsets of a set of n elements."""
    if n == 0:
        return [[]]
    else:
        remaining_subsets = recursion(n - 1)
        return remaining_subsets + [subset + [n] for subset in remaining_subsets]


assert set(frozenset(x) for x in iteration(3)) == set(frozenset(x) for x in [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
assert set(frozenset(x) for x in recursion(3)) == set(frozenset(x) for x in [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])