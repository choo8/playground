def iteration(n: int) -> list[list[int]]:
    """Generate permutations of elements from 1 to n iteratively via depth first search by passing state."""
    results = []

    stack = [([], [False] * (n + 1))]
    while stack:
        prefix, selected = stack.pop()
        if len(prefix) == n:
            results.append(list(prefix))
        else:
            for i in range(1, n + 1):
                if selected[i]:
                    continue
                selected[i] = True
                stack.append((prefix + [i], list(selected)))
                selected[i] = False

    return results


def recursion(nums: list[int]) -> list[list[int]]:
    """Generate permutations of `nums` recursively."""
    if not nums:
        return [[]]
    else:
        permutations = []
        for i, first in enumerate(nums):
            remaining_elements = nums[:i] + nums[i + 1:]
            permutations += [[first] + rest for rest in recursion(remaining_elements)]
        return permutations


assert set(frozenset(x) for x in iteration(3)) == set(frozenset(x) for x in [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
assert set(frozenset(x) for x in recursion([1, 2, 3])) == set(frozenset(x) for x in [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])