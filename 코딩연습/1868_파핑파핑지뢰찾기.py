movement = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [1, -1], [-1, 1], [1, 1]]   # 상하좌우 좌상 우상 좌하 우하

for TC in range(int(input())):
    N = int(input())
    mine_table = [list(input()) for i in range(N)]
    # cnt_table = [[0] * N for i in range(N)]

    click = 0

    # for y in range(N):
    #     for x in range(N):
    #         if mine_table[y][x] == '.':
    #             click += 1
    #             mine_table[y][x] = '*'
    #             stack = [[x, y]]
    #             while stack:
    #                 flag = 1
    #                 mine_stack = []
    #                 for move in movement:
    #                     nx, ny = x + move[0], y + move[1]
    #                     if -1 < nx < N and -1 < ny < N:
    #                         if mine_table[ny][nx] == '.':
    #                             stack.append([nx, ny])
    #                         else:
    #                             flag = 0
    #                             mine_stack.append([nx, ny])
    #                 if flag:
    #                     pass
    #                 else:
    #                     i = 0
    #                     while True:
    #                         for mine in mine_stack:

    # 처음에 그냥 단순하게 주위에 0이 되는 점을 찾아 스택에 넣고,
    # 해당 점의 주위에 0이 되는 점을 찾아 스택에 넣고, 주위 8칸을 모두 .에서 *로 변경 (이를 반복)

    # cnt table을 만들어서 하자
    for y in range(N):
        for x in range(N):
            if mine_table[y][x] == '.':
                cnt = 0
                for move in movement:
                    nx, ny = x + move[0], y + move[1]
                    if -1 < nx < N and -1 < ny < N:
                        if mine_table[ny][nx] == '*':
                            cnt += 1
                mine_table[y][x] = cnt

    for y in range(N):
        for x in range(N):
            if not mine_table[y][x] == '*':
                # 이제 여기서 순회하면서 주위에 0이 있다면 stack에 넣고,
                # 하나씩 꺼내서 0짜리라면 누른 다음 상하좌우는 무조건 스택에 넣고
                # 0짜리가 아니면 누르고 상하좌우에 0이 있는지 보고