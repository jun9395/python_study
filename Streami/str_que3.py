# 각각 N개의 정수를 담고 있는 arrays A, B
# A와 B를 C로 merge하고 싶다
# index K (0부터 N-1까지)에 대해서 C[K]는 A[K] 아니면 B[K]야 한다

# 예를 들어, A = [1, 2, 4, 3], B = [1, 3, 2, 3]이면
# C = [1, 3, 4, 3]이다
# 우리의 목표는 이렇게 만들어진 C에 포함되지 않는 최소 양의 정수를 찾는 것이다


def solution(A, B):
    # A, B의 길이는 1 이상 10만 이하, 각각의 원소 또한 마찬가지
    # C[K]가 A[K] 또는 B[k]가 되도록 A, B의 합성배열 C를 만들고,
    # C에 포함되지 않는 최소 양의 정수를 찾는 것이 목표
    # C부터 만들자. 큰 것을 넣어야 작은 것을 찾을 수 있게 된다
    n = len(A)
    i = 0
    C = []
    while i < n:
        if A[i] > B[i]:
            C.append(A[i])
        else:
            C.append(B[i])
        i += 1

    # C에 없는 최소 양의 정수를 찾자
    C.sort()
    smallest = 1
    i = 0
    while C[i] <= 0:
        i += 1
    for j in range(i, len(C)):
        if C[j] < smallest:
            continue
        elif C[j] == smallest:
            smallest += 1
        else:
            break
    return smallest

testcase = [[[1, 2, 4, 3], [1, 3, 2, 3]], [[3, 2, 1, 6, 5], [4, 2, 1, 3, 3]]]

for AB in testcase:
    print(solution(AB[0], AB[1]))