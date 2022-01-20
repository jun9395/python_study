hexs = ['A', 'B', 'C', 'D', 'E', 'F']


def solution(n, t, m, p):   # n진수, t개, m명, p번째
    p -= 1
    if p == 0:
        answer = '0'
    else:
        answer = ''

    cnt = 0
    num = 1
    while len(answer) < t:
        new = ''
        copy = num
        while copy > 0:
            rem = copy % n
            if rem < 10:
                new += str(rem)
            else:
                new += hexs[rem - 10]
            copy = int(copy / n)

        if cnt + len(new) >= p :
            new = new[::-1]
            idx = (m - 1 - cnt + p) % m
            while idx < len(new):
                answer += new[idx]
                if len(answer) >= t:
                    return answer
                idx += m
            cnt = (cnt + len(new)) % m
        else:
            cnt += len(new)

        num += 1

    return answer


n = 16
t = 16
m = 2
p = 2

print(solution(n, t, m, p))