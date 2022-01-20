def solution(n, times):
    small = 0
    large = times[0] * n
    middle = int((small + large) / 2)
    while small != middle and middle != large:
        people = 0
        for time in times:
            people += middle//time
        if people < n:
            small = middle
        else:
            large = middle
        middle = int((small + large) / 2)
    return large



# n = 8
# [4, 7, 10]
# 1번째 사람은 0에 가서 4에 끝남 [0, 4]
# 2번째 사람은 4에 가서 8에 끝남 [0, 4, 8]
# 3번째 사람은 0에 가서 7에 끝남 [0, 7]
# 4번째 사람은 0에 가서 10에 끝남 [0, 10]
# 5번째 사람은 8에 가서 12에 끝남 [0, 4, 8, 12]
# 6번째 사람은 7에 가서 14에 끝남 [0, 7, 14]
# 7번째 사람은 12에 가서 16에 끝남 [0, 4, 8, 12, 16]
# 8번째 사람은 16에 가서 20에 끝남 [0, 4, 8, 12, 16, 20]

# 4끝, 7끝, 10끝 -> 0
# 7끝, 8끝, 10끝 -> 1
# 8끝, 10끝, 14끝 -> 2
# 10끝, 12끝, 14끝 -> 3
# 12끝, 14끝, 20끝 -> 4
# 14끝, 16끝, 20끝 -> 5
# 16끝, 20끝, 21끝 -> 6
# 20끝, 20끝, 21끝 -> 7
# 20끝, 21끝, 24끝 -> 8


# import heapq


# def solution(n, times):
#     heap = []
#     for time in times:
#         heapq.heappush(heap, [time, time])
#     while n > 0:
#         n -= 1
#         end, time = heapq.heappop(heap)
#         heapq.heappush(heap, [end + time, time])

#     return end
