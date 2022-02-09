from collections import deque

moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def FindStart(board):
    x, y, n, m = -1, -1, -1, -1
    for j in range(len(board)):
        for i in range(len(board[0])):
            if x > 0 and n > 0:
                return x, y, n, m
            if board[j][i] == 2:
                x, y = i, j
            elif board[j][i] == 3:
                n, m = i, j
    return x, y, n, m


def solution(board, c):
    row = len(board)
    col = len(board[0])
    x, y, n, m = FindStart(board)
    stack = deque()
    stack.append((x, y, 0))
    visited = [[0] * col for _ in range(row)]
    visited[y][x] = 1

    while stack:
        x, y, cost = stack.popleft()

        cost += 1
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if -1 < nx < col and -1 < ny < row:
                if board[ny][nx] == 1:
                    if visited[ny][nx] == 0 or visited[ny][nx] > cost + c:
                        visited[ny][nx] = cost + c
                        stack.append((nx, ny, cost + c))
                else:
                    if visited[ny][nx] == 0 or visited[ny][nx] > cost:
                        visited[ny][nx] = cost
                        stack.append((nx, ny, cost))

    return visited[m][n]



board = [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 3, 0, 0, 0, 1, 0]]
c = 1
# result = 9

print(solution(board, c))