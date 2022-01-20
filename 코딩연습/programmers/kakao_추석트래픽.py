def IsItBigger(criterion, checks):
    if criterion[0] < checks[0]:
        return True
    elif criterion[0] == checks[0]:
        if criterion[1] < checks[1]:
            return True
        elif criterion[1] == checks[1]:
            if criterion[2] < checks[2]:
                return True
            elif criterion[2] == checks[2]:
                if criterion[3] < checks[3]:
                    return True
    return False


def IsItSmaller(criterion, checks):
    if criterion[0] > checks[0]:
        return True
    elif criterion[0] == checks[0]:
        if criterion[1] > checks[1]:
            return True
        elif criterion[1] == checks[1]:
            if criterion[2] > checks[2]:
                return True
            elif criterion[2] == checks[2]:
                if criterion[3] > checks[3]:
                    return True
    return False


def ParsingTimes(dates):
    date, end, need = dates.split(' ')
    ends = end.split(':')
    ends[0] = int(ends[0])          # 시간
    ends[1] = int(ends[1])          # 분
    ends.append(int(ends[2][3:]))   # 초
    ends[2] = int(ends[2][:2])      # 밀리초

    needs = list(map(int, need[:len(need) - 1].split('.')))

    starts = list(ends)
    for idx in range(len(needs)):
        starts[2 + idx] -= needs[idx]
    starts[3] += 1

    if starts[3] < 0:
        starts[3] = 1000 + starts[3]
        starts[2] -= 1
    for idx in range(2, 0, -1):
        if starts[idx] < 0:
            starts[idx] = 60 + starts[idx]
            starts[idx - 1] -= 1

    return starts, ends


def GetStimeEtime(times):
    start = list(times)
    end = list(times)
    start[2] -= 1
    if start[2] < 0:
        start[2] = 60 + start[2]
        start[1] -= 1
        if start[1] < 0:
            start[1] = 60 + start[1]
            start[0] -= 1
    start[3] += 1
    end[2] += 1
    end[3] -= 1
    if end[3] < 0:
        end[3] = 1000 + end[3]
        end[2] -= 1
        if end[2] < 0:
            end[2] = 60 + end[2]
            end[1] -= 1
            if end[1] < 0:
                end[1] = 60 + end[1]
                end[0] -= 1
    return start, end


def solution(lines):
    time_table = []
    time_stamp = []

    for line in lines:
        start, end = ParsingTimes(line)
        time_table.append(start)
        time_table.append(end)
        time_stamp.append([start, end])

    time_table.sort()
    time_stamp.sort()
    answer = 0
    for times in time_table:
        # 각 시간마다 앞 1초, 뒤 1초
        s_times, e_times = GetStimeEtime(times)

        pre_answer = 0
        post_answer = 0
        for checks in time_stamp:
            flag1 = IsItSmaller(s_times, checks[1])
            if flag1:
                continue
            else:
                flag2 = IsItBigger(times, checks[0])
                if flag2:
                    continue
                else:
                    pre_answer += 1

            flag3 = IsItSmaller(times, checks[1])
            if flag3:
                continue
            else:
                flag4 = IsItBigger(e_times, checks[0])
                if flag4:
                    break
                else:
                    post_answer += 1

        if answer < pre_answer:
            answer = pre_answer
        if answer < post_answer:
            answer = post_answer

    return answer


lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
# lines = ["2016-09-15 23:59:59.999 0.001s"]

print(solution(lines))


# def IsItBigger(criterion, checks):
#     if criterion[0] < checks[0]:
#         return True
#     elif criterion[0] == checks[0]:
#         if criterion[1] < checks[1]:
#             return True
#         elif criterion[1] == checks[1]:
#             if criterion[2] < checks[2]:
#                 return True
#             elif criterion[2] == checks[2]:
#                 if criterion[3] < checks[3]:
#                     return True
#     return False
#
#
# def IsItSmaller(criterion, checks):
#     if criterion[0] > checks[0]:
#         return True
#     elif criterion[0] == checks[0]:
#         if criterion[1] > checks[1]:
#             return True
#         elif criterion[1] == checks[1]:
#             if criterion[2] > checks[2]:
#                 return True
#             elif criterion[2] == checks[2]:
#                 if criterion[3] > checks[3]:
#                     return True
#     return False
#
#
# def ParsingTimes(dates):
#     date, end, need = dates.split(' ')
#     ends = end.split(':')
#     ends[0] = int(ends[0])          # 시간
#     ends[1] = int(ends[1])          # 분
#     ends.append(int(ends[2][3:]))   # 초
#     ends[2] = int(ends[2][:2])      # 밀리초
#
#     needs = list(map(int, need[:len(need) - 1].split('.')))
#
#     starts = list(ends)
#     for idx in range(len(needs)):
#         starts[2 + idx] -= needs[idx]
#     starts[3] += 1
#
#     if starts[3] < 0:
#         starts[3] = 1000 + starts[3]
#         starts[2] -= 1
#     for idx in range(2, 0, -1):
#         if starts[idx] < 0:
#             starts[idx] = 60 + starts[idx]
#             starts[idx - 1] -= 1
#
#     return starts, ends
#
#
# def solution(lines):
#     time_table = []
#     time_stamp = []
#
#     for line in lines:
#         start, end = ParsingTimes(line)
#         time_table.append(start)
#         time_table.append(end)
#         time_stamp.append([start, end])
#
#     time_table.sort()
#     time_stamp.sort()
#     answer = 0
#     for times in time_table:
#         # 각 시간마다 앞 1초, 뒤 1초
#         start = list(times)
#         end = list(times)
#         start[2] -= 1
#         if start[2] < 0:
#             start[2] = 60 + start[2]
#             start[1] -= 1
#             if start[1] < 0:
#                 start[1] = 60 + start[1]
#                 start[0] -= 1
#         start[3] += 1
#         end[2] += 1
#         end[3] -= 1
#         if end[3] < 0:
#             end[3] = 1000 + end[3]
#             end[2] -= 1
#             if end[2] < 0:
#                 end[2] = 60 + end[2]
#                 end[1] -= 1
#                 if end[1] < 0:
#                     end[1] = 60 + end[1]
#                     end[0] -= 1
#
#         pre_answer = 0
#         post_answer = 0
#         for checks in time_stamp:
#             flag1 = IsItSmaller(start, checks[1])
#             if flag1:
#                 continue
#             else:
#                 flag2 = IsItBigger(times, checks[0])
#                 if flag2:
#                     break
#                 else:
#                     pre_answer += 1
#         for checks in time_stamp:
#             flag3 = IsItSmaller(times, checks[1])
#             if flag3:
#                 continue
#             else:
#                 flag4 = IsItBigger(end, checks[0])
#                 if flag4:
#                     break
#                 else:
#                     post_answer += 1
#
#         if answer < pre_answer:
#             answer = pre_answer
#         if answer < post_answer:
#             answer = post_answer
#
#     return answer
