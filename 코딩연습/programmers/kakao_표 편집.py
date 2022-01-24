def solution(n, k, cmd):
    table = []
    check = dict()
    for i in range(n):
        table.append([i - 1, i + 1])
        check[i] = True
    select = k
    stack = []

    for temp in cmd:
        moves = temp.split()
        if moves[0] == 'C':
            pre = table[select][0]
            post = table[select][1]
            if -1 < pre:
                table[pre][1] = post
            if post < n:
                table[post][0] = pre
            stack.append(select)
            check[select] = False
            if post < n:
                select = post
            else:
                select = pre
        elif moves[0] == 'Z':
            restore = stack.pop()
            check[restore] = True
            pre = table[restore][0]
            post = table[restore][1]
            if -1 < pre:
                table[pre][1] = restore
            if post < n:
                table[post][0] = restore
        else:
            if moves[0] == 'U':
                for move in range(int(moves[1])):
                    select = table[select][0]
            else:
                for move in range(int(moves[1])):
                    select = table[select][1]

    answer = []
    for i in range(n):
        if check.get(i):
            answer.append('O')
        else:
            answer.append('X')

    return ''.join(answer)


cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
n = 8
k = 2

print(solution(n, k, cmd))

# 효율성 6~10 시간초과
# def MoveCmd(key, move, now, answer):
#     count = 0
#     while count < move:
#         if key == 'U':
#             now -= 1
#         else:
#             now += 1
#         if answer[now] == 'O':
#             count += 1
#     return now
#
#
# def solution(n, k, cmd):
#     answer = ['O'] * n
#     stack = []
#     select = k
#     end = n - 1
#
#     for temp in cmd:
#         moves = temp.split()
#         if moves[0] == 'C':
#             answer[select] = 'X'
#             stack.append(select)
#             if select < end:
#                 while answer[select] == 'X':
#                     select += 1
#             else:
#                 while answer[select] == 'X':
#                     select -= 1
#                 end = select
#         elif moves[0] == 'Z':
#             last = stack.pop()
#             answer[last] = 'O'
#             if end < last:
#                 end = last
#         else:
#             select = MoveCmd(moves[0], int(moves[1]), select, answer)
#
#     return ''.join(answer)