from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    answer = len(words)
    n = len(begin)

    stack = deque()
    stack.append((begin, 0, [begin]))
    while stack:
        now, step, visited = stack.popleft()
        # if now == target:
        #     return step
        for word in words:
            if word not in visited:
                count = 0
                for i in range(n):
                    if now[i] != word[i]:
                        count += 1
                        if count > 1:
                            break
                if count == 1:
                    if word == target:
                        return step + 1
                    stack.append((word, step + 1, visited + [word]))

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))
