def solution(n):
    flag1 = 1
    flag2 = 2
    for idx in range(2, n):
        flag1, flag2 = flag2, flag1 + flag2

    return flag2 % 1_000_000_007

n = 4

print(solution(n))


# def FillTile(check, m):
#     if check[m] > 0:
#         return check[m]
#
#     check[m] = FillTile(check, m - 1) + FillTile(check, m - 2)
#     return check[m]
#
#
# def solution(n):
#     check = [-1] * n
#     check[0] = 1
#     check[1] = 2
#     FillTile(check, n - 1)
#
#     return check[n - 1] % 1_000_000_007