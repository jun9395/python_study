for TC in range(int(input())):
    N, Q = map(int, input().split())
    cups = [0] * (N + 1)
    cups[1] = 1
    chance = 1
    stack = [[cups, chance]]    # 컵의 현재 상태, 남은 속임수 획수

    for i in range(Q):
        a, b = map(int, input().split())


    # while stack:
    #     cups, chance = stack.pop()
    #     if chance:
    #
    #     else:
    #         pass
