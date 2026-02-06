def water_jug_dfs(a, b, c, target):
    visited = set()
    path = []

    def dfs(x, y, z):
        if (x, y, z) in visited:
            return False

        visited.add((x, y, z))
        path.append((x, y, z))

        if x == target or y == target or z == target:
            return True

        next_states = [
            (a, y, z), (x, b, z), (x, y, c),
            (0, y, z), (x, 0, z), (x, y, 0),

            (x - min(x, b - y), y + min(x, b - y), z),
            (x - min(x, c - z), y, z + min(x, c - z)),
            (x + min(y, a - x), y - min(y, a - x), z),
            (x, y - min(y, c - z), z + min(y, c - z)),
            (x + min(z, a - x), y, z - min(z, a - x)),
            (x, y + min(z, b - y), z - min(z, b - y))
        ]

        for state in next_states:
            if dfs(*state):
                return True

        path.pop()   # backtrack
        return False

    return path if dfs(0, 0, 0) else None


# Example
result = water_jug_dfs(8, 5, 3, 4)
print(result)
