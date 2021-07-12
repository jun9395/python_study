def solution(s):
    stack = []
    for i in range(len(s)):
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    if stack:
        return 0
    return 1
    # idx = 0
    # while idx < len(s) - 1:
    #     if s[idx] == s[idx + 1]:
    #         s = s[:idx] + s[idx + 2:]
    #         if idx > 0:
    #             idx -= 1
    #     else:
    #         idx += 1
    # if len(s):
    #     return 0
    # return 1


s = "abbcaacbba"    # 답은 1

print(solution(s))
