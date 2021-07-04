# 1 <= i <= (n+1)/2인 모든 자연수 i에 대해서 s(i) = s(n - i + 1)

def solution(s):
    answer = []
    i = 0
    n = len(s)
    flag = 0
    while i < int(n/2):
        j = 1
        flag = 0
        while True:
            if s[i:i + j] == s[n - i - j:n - i]:
                if i + j > n - i - j:
                    flag = 1
                break
            j += 1

        answer.append(s[i:i + j])
        i += j

    anti = list(reversed(answer))
    if flag:
        anti = anti[1:]


    return answer + anti


# s = "abcxyasdfasdfxyabc"
# s = "abcxyqwertyxyabc"
# s = "abcabcabcabc"
s = "llttaattll"
# s = "zzzzzz"
# s = "abcdef"


print(solution(s))
