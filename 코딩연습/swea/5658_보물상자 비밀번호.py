import sys
sys.stdin = open("sample_input.txt", "r")

HEX = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def GetHexNum(numbers, m):
    number = 0
    idx = m - 1
    hex_n = 1
    while idx > -1:
        if HEX.get(numbers[idx]):
            number += HEX[numbers[idx]] * hex_n
        else:
            number += int(numbers[idx]) * hex_n
        idx -= 1
        hex_n *= 16

    return number


def IsAllIn(nows, firsts):
    for number in nows:
        if not firsts.get(number):
            return False
    return True


for TC in range(int(input())):
    n, k = map(int, input().strip().split())
    m = n // 4
    numbers = list(input()[:n])
    answers = set()

    first_numbers = dict()
    idx = 0
    while idx < n:
        number = GetHexNum(numbers[idx: idx+m], m)
        first_numbers[number] = True
        answers.add(number)
        idx += m

    while True:
        now_numbers = []
        numbers = [numbers[n - 1]] + numbers[:n - 1]
        idx = 0
        while idx < n:
            number = GetHexNum(numbers[idx: idx+m], m)
            now_numbers.append(number)
            answers.add(number)
            idx += m

        flag = IsAllIn(now_numbers, first_numbers)
        if flag:
            break

    answer = sorted(list((answers)), reverse=True)
    print('#{} {}' .format(TC + 1, answer[k - 1]))
