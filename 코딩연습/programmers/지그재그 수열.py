def solution(s):
    n = len(s)
    updown = True  # True면 현재 값이 이전 값보다 커야 한다
    answer = 0
    for i in range(1, n):
        if updown:
            if s[i] <= s[i - 1]:
                answer += 1
            else:
                updown = False
        else:
            if s[i] >= s[i - 1]:
                answer += 1
            else:
                updown = True

    return answer


# s = [1, 2, 3]   # result = 1
# s = [3, -1, 0, 4]   # result = 2
# s = [0, -2, -1, 3, 5, 6, 7]     # result = 5
s = [1, 2, 2, 3, 3, 3, 3, 3]    # result = 6

print(solution(s))
