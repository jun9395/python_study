# 같은 시간에 번식 -> 생명력이 높은 쪽으로 대체
# 투입시간 + 생명력 + 1 -> 번식, 즉 새로운 투입시간 = 이전 투입시간 + 생명력
# 투입시간 + 생명력 * 2 -> 사망
# 번식시간 = 투입시간 + 생명력
# 일단 꺼내서 상하좌우에 번식하게 stack에 쌓고
# 단, 투입시간이 K 리미트를 초과하면 stack에 안 넣는다
# 살았는지 죽었는지는 마지막에 체크
# stack에 들어갈 내용은 ((위치)))
# (위치)를 key로 투입시간을 체크할 dict
# (위치)를 key로 생명력을 체크할 dict
# 끝나는 시간 k < 투입시간 + 생명력 * 2면 살아있다

# 통과는 됐으나, 시간이 13초 정도 걸린다
# 매 초마다 dict을 전부 순회하는 것이 원인으로 보임
# 이를 수정하면 되지 않을까? -> 해결
from collections import deque

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


for TC in range(int(input())):
    insert_times = dict()
    lifes = dict()
    row, col, k = map(int, input().strip().split())
    table = []
    for _ in range(row):
        table.append(list(map(int, input().strip().split()))[:col])

    stack = deque()
    for y in range(row):
        for x in range(col):
            if table[y][x] > 0:
                stack.append((x, y))
                insert_times[(x, y)] = 0
                lifes[(x, y)] = table[y][x]

    t = 0
    while t < k - 1:
        t += 1
        n = len(stack)
        for i in range(n):
            x, y = stack.popleft()
            if insert_times[(x, y)] + lifes[(x, y)] == t:
                for move in moves:
                    nx, ny = x + move[0], y + move[1]
                    if insert_times.get((nx, ny)) is not None:
                        if insert_times[(nx, ny)] == t + 1:
                            if lifes[(nx, ny)] < lifes[(x, y)]:
                                lifes[(nx, ny)] = lifes[(x, y)]
                    else:
                        insert_times[(nx, ny)] = t + 1
                        lifes[(nx, ny)] = lifes[(x, y)]
                        stack.append((nx, ny))
            else:
                stack.append((x, y))
        # for (x, y) in list(insert_times.keys()):
        #     if insert_times[(x, y)] + lifes[(x, y)] == t:
        #         for move in moves:
        #             nx, ny = x + move[0], y + move[1]
        #             if insert_times.get((nx, ny)) is not None:
        #                 if insert_times[(nx, ny)] == t + 1:
        #                     if lifes[(nx, ny)] < lifes[(x, y)]:
        #                         lifes[(nx, ny)] = lifes[(x, y)]
        #             else:
        #                 insert_times[(nx, ny)] = t + 1
        #                 lifes[(nx, ny)] = lifes[(x, y)]

    answer = 0
    answers = []
    for position, insert in insert_times.items():
        if k < insert + 2 * lifes[position]:
            answer += 1
            answers.append(lifes[position])

    print("#{} {}" .format(TC + 1, answer))
