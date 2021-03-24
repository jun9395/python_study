for TC in range(int(input())):
    p, q = map(int, input().split())
    now, future = 1, 1
    term = 1    # y축 값의 간격을 나타내면서, 동시에 y축의 높이를 뜻함
    p_pos, q_pos = 0, 0

    while not (p_pos and q_pos):
        future += term
        if now <= p < future:
            diff = p - now
            p_pos = [diff + 1, term - diff]
        if now <= q < future:
            diff = q - now
            q_pos = [diff + 1, term - diff]
        now = future
        term += 1

    p_pos[0] += q_pos[0]
    p_pos[1] += q_pos[1]

    line = p_pos[0] + p_pos[1] - 1  # 몇 번째 라인에 있는지 확인. 1,1의 경우 1번째 라인이고, 3,3의 경우 5번째 라인이다
    ans = 0

    while not ans:
        future += term
        term += 1
        if term == line:
            ans = future + p_pos[0] - 1

    print('#{} {}' .format(TC + 1, ans))