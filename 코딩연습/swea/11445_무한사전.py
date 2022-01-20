for TC in range(int(input())):
    P = input().strip()
    Q = input().strip()
    flag = 1
    i = len(P)

    if P != Q[:i]:
        flag = 0

    if flag:
        if len(Q) - 1 > i:
            print('#{} {}' .format(TC + 1, 'Y'))
        elif Q[i] == 'a':
            print('#{} {}' .format(TC + 1, 'N'))
        else:
            print('#{} {}' .format(TC + 1, 'N'))
    else:
        print('#{} {}' .format(TC + 1, 'Y'))
