num_dict = {
    "ze" : ["0", 4],
    "on" : ["1", 3],
    "tw" : ["2", 3],
    "th" : ["3", 5],
    "fo" : ["4", 4],
    "fi" : ["5", 4],
    "si" : ["6", 3],
    "se" : ["7", 5],
    "ei" : ["8", 5],
    "ni" : ["9", 4]
}


def solution(s):
    n = 0
    answer = ""
    while n < len(s):
        if "0" <= s[n] <= "9":
            answer += s[n]
            n += 1
        else:
            keyword = s[n] + s[n + 1]
            answer += num_dict[keyword][0]
            n += num_dict[keyword][1]
    return int(answer)