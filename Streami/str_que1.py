# def solution(A):
#     # write your code in Python 3.6
#     A.sort()
#     smallest = 1
#     i = 0
#     while A[i] <= 0:
#         i += 1
#     for j in range(i, len(A)):
#         if A[j] < smallest:
#             continue
#         elif A[j] == smallest:
#             smallest += 1
#         else:
#             break
#     return smallest
#
#
# A = [-1, -3]
#
# print(solution(A))


# solution에서 버그를 찾고 수정하라.
# 최대 1000개의 정수 [-1000..1000]을 갖는 비지 않은 Array A에서
# 최소 element를 찾는 solution

# A 정수들 들어있는 행렬
# 오류가 나는데 찾아서 고쳐라

def solution(A):
    minvalue = 0
    for i in range(1, len(A)):
        if minvalue > A[i]:
            minvalue = A[i]
    return minvalue
