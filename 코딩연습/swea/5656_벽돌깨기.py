# import sys
from collections import deque

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# sys.stdin = open("sample_input.txt", "r")


def Straighten(end, table_line):
    for start in range(end - 1, -1, -1):
        if table_line[start] > 0:
            table_line[start], table_line[end] = table_line[end], table_line[start]
            return False
    return True


def Bombs(a, b, value, mapping):
    fires = deque()
    checks = {(a, b): True}
    fires.append((a, b, mapping[b][a]))
    mapping[b][a] = 0
    value += 1

    while fires:
        a, b, powers = fires.popleft()
        # powers = mapping[b][a]
        for power in range(1, powers):
            for move in moves:
                nx, ny = a + move[0] * power, b + move[1] * power
                if -1 < nx < len(mapping[0]) and -1 < ny < len(mapping):
                    if mapping[ny][nx] and not checks.get((nx, ny)):
                        checks[(nx, ny)] = True
                        fires.append((nx, ny, mapping[ny][nx]))
                        mapping[ny][nx] = 0
                        value += 1

    return value


for TC in range(int(input())):
    n, w, h = map(int, input().split(' '))
    old_table = []
    block = 0
    for y in range(h):
        old_table.append(list(map(int, input().strip().split(' ')))[:w])
        for num in old_table[y]:
            if num > 0:
                block += 1

    ori_table = []
    for x in range(w):
        temp = list()
        for y in range(h):
            temp.append(old_table[y][x])
        ori_table.append(temp)

    # 이제 가로가 h, 세로가 w
    answer = block
    stack = deque()
    stack.append((n, 0, ori_table))
    while stack:
        count, score, old_table = stack.popleft()

        for y in range(w):
            for x in range(h):
                if old_table[y][x] > 0:
                    broken = old_table[y][x]
                    table = list()
                    for _ in range(w):
                        table.append(list(old_table[_]))

                    new_score = Bombs(x, y, score, table)
                    if count > 1:
                        if block == new_score:
                            answer = 0
                        else:
                            if broken > 1:
                                for j in range(w):
                                    for i in range(h):
                                        if table[j][h - 1 - i] == 0:
                                            if Straighten(h - 1 - i, table[j]):
                                                break
                            stack.append((count - 1, new_score, table))
                    else:
                        if answer > block - new_score:
                            answer = block - new_score

                    break

    print('#{} {}' .format(TC + 1, answer))


# def Straighten(start, table_line):
#     for x in range(start + 1, len(table_line)):
#         if table_line[x] > 0:
#             table_line[start], table_line[x] = table_line[x], table_line[start]
#             return False
#     return True
#
#
# def MakeTable(x, y, score, table):
#     check = {(x, y): True}
#     bombs = deque()
#     bombs.append((x, y))
#
#     while bombs:
#         x, y = bombs.popleft()
#         fires = table[y][x]
#         table[y][x] = 0
#         score += 1
#         for fire in range(fires):
#             for move in moves:
#                 nx, ny = x + fire * move[0], y + fire * move[1]
#                 if -1 < nx < len(table[0]) and -1 < ny < len(table):
#                     if not check.get((nx, ny)):
#                         check[(nx, ny)] = True
#                         bombs.append((nx, ny))
#
#     return score
#
#
# for TC in range(int(input())):
#     answer = 0
#     n, w, h = map(int, input().split(' '))  # h 가로, w 세로
#     # 테이블 인풋값을 시계방향으로 90도 회전하는 작업
#     table = []
#     for y in range(h):
#         table.append(list(map(int, input().strip().split(' ')))[:w])
#     ori_table = []
#     for x in range(w):
#         temp = list()
#         for y in range(h):
#             temp.append(table[h - 1 - y][x])
#         ori_table.append(temp)
#
#     stack = deque()
#     stack.append((n, 0, ori_table))
#
#     while stack:
#         count, score, ori_table = stack.popleft()
#         for y in range(w):
#             for x in range(h):
#                 if ori_table[y][h - 1 - x] > 0:
#                     table = list()
#                     for _ in range(w):
#                         table.append(list(ori_table[_]))    # 깊은 복사
#                     new_score = MakeTable(h - 1 - x, y, score, table)
#                     if count > 1:
#                         for j in range(w):
#                             for i in range(h):
#                                 if table[j][i] == 0:
#                                     if Straighten(i, table[j]):
#                                         break
#                         stack.append((count - 1, new_score, table))
#                     else:
#                         if answer < new_score:
#                             answer = new_score
#                     break
#
#     # print(f'#{TC + 1} {answer}')
#     print('#{} {}' .format(TC + 1, answer))
