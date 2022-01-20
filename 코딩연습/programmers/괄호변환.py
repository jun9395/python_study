def check(stc):
    stack = []
    for cha in stc:
        if cha == '(':
            stack.append(cha)
        elif cha == ')':
            if stack and stack[len(stack) - 1] == '(':
                stack.pop()
            else:
                return False
    return True


def solution(p):
    N = len(p)
    answer = ''
    idx = 0
    left = 0
    right = 0

    if N:
        while idx < N:
            if p[idx] == '(':
                left += 1
            elif p[idx] == ')':
                right += 1
            if left == right:
                break
            idx += 1
        u = p[:idx + 1]
        v = p[idx + 1:]

        if check(u):
            return u + solution(v)
        else:
            answer += '('
            answer += solution(v)
            answer += ')'
            for i in range(1, len(u) - 1):
                if u[i] == '(':
                    answer += ')'
                else:
                    answer += '('

    return answer