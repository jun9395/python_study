# 0 이상의 2진 숫자 V를 encode한 길이 N의 string S
# V가 홀수면 1을 빼라
# V가 짝수면 2로 나누어라
# V가 0이 될 때까지 시도하라
# S = "011100"이면 V은 28이었다.

# 정수 V로부터 얻어진 길이 N의 S가 주어졌을 때
# 오퍼레이션 횟수를 적어라

# S = "111"이면 5를 return하라


# 예외처리 하나 해야한다
# 0의 경우가 제대로 안 된다


def solution(S):
    str_S = list(S)[::-1]
    now = 0
    count = 0
    while now < len(str_S):
        count += 1
        if str_S[now] == '1':
            str_S[now] = '0'
        else:
            now += 1
    return count

# S = "011100"
S = "0"

print(solution(S))