from collections import deque

def water_jug_bfs(a, b, c, target):
    start = (0, 0, 0)
    queue = deque()
    queue.append((start, []))
    visited = set()

    while queue:
        (x, y, z), path = queue.popleft()

        if (x, y, z) in visited:
            continue
        visited.add((x, y, z))

        path = path + [(x, y, z)]

        if x == target or y == target or z == target:
            return path

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
            if state not in visited:
                queue.append((state, path))

    return None

result = water_jug_bfs(8, 5, 3, 4)
print(result)
