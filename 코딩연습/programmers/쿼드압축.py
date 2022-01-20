# 고민하느라 1시간30분 정도 걸림


def solution(arr):
    if len(arr) == 1:
        if arr[0][0]:
            return [0, 1]
        return [1, 0]
    
    n = len(arr)
    N = n * n
    one_count = 0
    for quad in arr:
        one_count += sum(quad)
    zero_count = N - one_count
    
    if not zero_count:
        return [0, 1]
    elif not one_count:
        return [1, 0]
    else:
        cut = int(n / 2)
        quads = [[], [], [], []]
        for y in range(n):
            if y < cut:
                quads[0].append([])
                quads[1].append([])
                for x in range(n):
                    if x < cut:
                        quads[0][y].append(arr[y][x])
                    else:
                        quads[1][y].append(arr[y][x])
            else:
                quads[2].append([])
                quads[3].append([])
                for x in range(n):
                    if x < cut:
                        quads[2][y - cut].append(arr[y][x])
                    else:
                        quads[3][y - cut].append(arr[y][x])
        first = solution(quads[0])
        second = solution(quads[1])
        third = solution(quads[2])
        fourth = solution(quads[3])
        return [first[0] + second[0] + third[0] + fourth[0], first[1] + second[1] + third[1] + fourth[1]]
