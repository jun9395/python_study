for TC in range(int(input())):
    D, M, T, Y = map(int, input().split())

    schedule = list(map(int, input().split()))
    i = 0
    j = len(schedule)
    while True:
        if i == j or schedule[i]:
            break
        i += 1
    schedule = schedule[i:]
    # schedule = list(filter(lambda x: x > 5, schedule))
    j = len(schedule) - 1
    while True and j > -1:
        if schedule[j]:
            break
        j -= 1
    schedule = schedule[:j + 1]

    # min_cost = Y
    works = len(schedule)
    cost_schedule = [0] * works

    # 하루씩 끊기 vs 한달씩 끊기
    for i in range(works):
        today = schedule[i] * D
        if today > M:
            cost_schedule[i] = M
        else:
            cost_schedule[i] = today

    i = 0
    while i < works:





    # j = len(schedule)
    #
    # # 하루하루 다 끊는 경우
    # now_cost = 0
    # for i in range(j):
    #     now_cost += schedule[i] * D
    #     if now_cost >= min_cost:
    #         break
    #
    # if now_cost < min_cost:
    #     min_cost = now_cost
    #
    # # 3개월치를 쓰는 경우
    # if j > 3:
    #     for i in range(j - 2):
    #         now_cost =
    #         for k in range(i):
    #             now_cost += schedule[i] * D
    #
    #
    # else:
        pass