from collections import deque

movement = [[0, -1], [0, 1], [-1, 0], [1, 0]]   # 상하좌우


def solution(maps):
    stack = deque()
    stack.append([0, 0, 0])
    maps[0][0] = 0
    n = len(maps)
    m = len(maps[0])

    while stack:
        x, y, step = stack.popleft()
        step += 1
        if x == m - 1 and y == n - 1:
            return step

        for move in movement:
            nx, ny = x + move[0], y + move[1]
            if -1 < nx < m and -1 < ny < n and maps[ny][nx]:
                stack.append([nx, ny, step])
                maps[ny][nx] = 0

    return -1