# 정확성 최대 시간 3.64ms
def solution(scoville, K):
    answer = 0
    scoville.sort()
    stack = list(reversed(scoville))
    
    minist = stack.pop()
    semini = stack.pop()
    
    while stack and minist < K:
        stack.append(minist + 2 * semini)
        stack.sort(reverse=True)
        answer += 1
        
        minist = stack.pop()
        semini = stack.pop()
    
    if minist >= K:
        return answer
    elif minist + 2 * semini >= K:
        return answer + 1
    return -1


# 정확성 최대 시간 41ms
# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     N = len(scoville) - 1
    
#     for now in range(N):
#         if scoville[now] >= K:
#             return answer
        
#         idx = now + 1
#         temp = scoville[now] + 2 * scoville[idx]
#         while N > idx and temp > scoville[idx]:
#             scoville[idx - 1] = scoville[idx]
#             idx += 1
#         if N == idx:
#             if scoville[N] > temp:
#                 scoville[idx - 1] = temp
#             else:
#                 scoville[idx - 1], scoville[idx] = scoville[idx], temp
#         else:
#             scoville[idx - 1] = temp
#         answer += 1
    
    
#     if scoville[N] >= K:
#         return answer
#     return -1