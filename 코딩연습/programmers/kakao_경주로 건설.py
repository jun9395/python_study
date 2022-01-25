from collections import deque

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 초기 answer를 안일하게 n * 1200로 한 것이 문제였다
def solution(board):
    n = len(board)
    answer = n * 1000000
    horizontal = dict()
    vertical = dict()
    stack = deque()
    stack.append((0, 0, 0, -1, -1))
    horizontal[(0, 0)] = 0
    vertical[(0, 0)] = 0

    while stack:
        x, y, money, go, back = stack.popleft()

        if money < answer:
            for idx in range(4):
                if idx != back:
                    nx, ny = x + moves[idx][0], y + moves[idx][1]
                    if -1 < nx < n and -1 < ny < n and board[ny][nx] == 0:
                        if idx == 0:
                            n_back = 2
                        elif idx == 1:
                            n_back = 3
                        elif idx == 2:
                            n_back = 0
                        else:
                            n_back = 1

                        n_money = money + 100
                        if -1 < go != idx:
                            n_money += 500

                        if idx % 2:
                            if vertical.get((nx, ny)):
                                if vertical[(nx, ny)] > n_money:
                                    vertical[(nx, ny)] = n_money

                                    if (nx, ny) == (n - 1, n - 1):
                                        if answer > n_money:
                                            answer = n_money
                                    else:
                                        stack.append((nx, ny, n_money, idx, n_back))
                            else:
                                vertical[(nx, ny)] = n_money
                                if (nx, ny) == (n - 1, n - 1):
                                    if answer > n_money:
                                        answer = n_money
                                else:
                                    stack.append((nx, ny, n_money, idx, n_back))
                        else:
                            if horizontal.get((nx, ny)):
                                if horizontal[(nx, ny)] > n_money:
                                    horizontal[(nx, ny)] = n_money

                                    if (nx, ny) == (n - 1, n - 1):
                                        if answer > n_money:
                                            answer = n_money
                                    else:
                                        stack.append((nx, ny, n_money, idx, n_back))
                            else:
                                horizontal[(nx, ny)] = n_money
                                if (nx, ny) == (n - 1, n - 1):
                                    if answer > n_money:
                                        answer = n_money
                                else:
                                    stack.append((nx, ny, n_money, idx, n_back))

    return answer


# board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

print(solution(board))


# 고치다가 최댓값 설정을 잘못한거 같아 확인해보니 위에꺼로도 되네
# def solution(board):
#     n = len(board)
#     answer = n * 1200
#     check = dict()
#     stack = deque()
#     stack.append((0, 0, 0, -1, -1))
#     check[(0, 0, -1)] = 0
#
#     while stack:
#         x, y, money, go, back = stack.popleft()
#
#         if (x, y) == (4, 5):
#             print()
#
#         if money < answer:
#             for idx in range(4):
#                 if idx != back:
#                     nx, ny = x + moves[idx][0], y + moves[idx][1]
#                     if -1 < nx < n and -1 < ny < n and board[ny][nx] == 0:
#                         if idx == 0:
#                             n_back = 2
#                         elif idx == 1:
#                             n_back = 3
#                         elif idx == 2:
#                             n_back = 0
#                         else:
#                             n_back = 1
#
#                         n_money = money + 100
#                         if -1 < go != idx:
#                             n_money += 500
#
#                         if check.get((nx, ny, idx)):
#                             if check[(nx, ny, idx)] > n_money:
#                                 check[(nx, ny, idx)] = n_money
#                                 if answer > n_money:
#                                     answer = n_money
#                                 else:
#                                     stack.append((nx, ny, n_money, idx, n_back))
#                         else:
#                             check[(nx, ny, idx)] = n_money
#                             if (nx, ny) == (n - 1, n - 1):
#                                 if answer > n_money:
#                                     answer = n_money
#                             else:
#                                 stack.append((nx, ny, n_money, idx, n_back))
#
#     return answer


# dfs는 시간 초과
#
# def dfs(board, check, x, y, go, back, money):
#     if check[1] < money or x == check[0] - 1 == y:
#         if check[1] > money:
#             check[1] = money
#         return
#
#     for idx in range(4):
#         if idx != back:
#             nx, ny = x + moves[idx][0], y + moves[idx][1]
#             if -1 < nx < check[0] and -1 < ny < check[0] and board[ny][nx] == 0:
#                 if idx == 0:
#                     n_back = 2
#                 elif idx == 1:
#                     n_back = 3
#                 elif idx == 2:
#                     n_back = 0
#                 else:
#                     n_back = 1
#
#                 n_money = money + 100
#                 if -1 < go != idx:
#                     n_money += 500
#
#                 if not check.get((nx, ny)):
#                     check[(nx, ny)] = True
#                     dfs(board, check, nx, ny, idx, n_back, n_money)
#                     check[(nx, ny)] = False
#
#
# def solution(board):
#     n = len(board)
#     # answer = n * 700
#     check = dict()
#     check[0] = n
#     check[1] = n * 700
#     check[(0, 0)] = True
#     dfs(board, check, 0, 0, -1, -1, 0)
#
#     return check[1]