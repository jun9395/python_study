def solution(s):
    n = len(s)

    for length in range(n, 0, -1):
        for idx in range(n + 1 - length):
            if s[idx: idx + length] == s[idx: idx + length][::-1]:
                return len(s[idx: idx + length])

    return 0


s = "abcdcba"

print(solution(s))
