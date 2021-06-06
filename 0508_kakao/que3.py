# def solution(n, k, cmd):
#     adict = dict()
#     k_del = []
#     for i in range(n):
#         adict[i] = True
#
#     first = 0   # 삭제하지 않은 행 중의 first인 값
#     f_num = 0   # 현재 k보다 작은 곳에서 false가 된 개수
#
#     for i in range(len(cmd)):
#         order = list(cmd[i].split())
#         if order[0] == "U":
#             k -= int(order[1]) + f_num
#         elif order[0] == "D":
#             k += int(order[1])
#         elif order[0] == "C":
#             flag = 0
#             adict[k] = False  # 현재 k의 위치를 제거(False)하고
#             if k == first:  # 현재 k의 위치가 first였으면 first를 옮겨야 한다
#                 flag = 1
#             k_del.append(k)  # k_del에 추가한다
#             while k < n:  # k가 n이랑 같으면 overflow
#                 k += 1
#                 f_num += 1
#                 if adict.get(k) == True:  # k값이 존재하면 탈출
#                     if flag:  # flag = 1이라는 얘기는 first를 바꿔줘야 한다는 말
#                         first = k
#                     break
#             if k == n:
#                 k = first
#                 f_num = first - 1
#                 if f_num < 0:
#                     f_num = 0
#         else:  # "Z"인 경우
#             restore = k_del.pop()  # 가장 최근에 지운 것을 복구
#             adict[restore] = True
#             if first > restore:  # 복구한 번호가 first보다 작다면 그게 최초값
#                 first = restore
#
#     answer = ''
#
#     for key in adict.keys():
#         if adict.get(key) == True:
#             answer += "O"
#         else:
#             answer += "X"
#
#     return answer




###############################################################

# def solution(n, k, cmd):
#     alist = [i for i in range(n)]  # [0, 1, 2, ..., n-1]
#     adict = dict()  # 마지막 answer를 만들 때 사용할 딕셔너리
#     for i in range(n):
#         adict[i] = True
#     k_deleted = []  # C로 제거하는 것을 차례대로 담을 리스트
#
#     for i in range(len(cmd)):
#         order = list(cmd[i].split())
#         if order[0] == "U":
#             k -= int(order[1])
#         elif order[0] == "D":
#             k += int(order[1])
#         elif order[0] == "C":
#             k_deleted.append(alist[k])
#             adict[alist[k]] = False
#             alist = alist[:k] + alist[k + 1:]
#             if k >= len(alist):
#                 k -= 1
#         else:  # Z인 경우, 최근 것부터 복구
#             restore = k_deleted.pop()
#             adict[restore] = True
#             if alist[k] > restore:
#                 k += 1
#             alist = alist[:restore] + [restore] + alist[restore:]
#
#     answer = ''
#
#     for key in adict.keys():
#         if adict.get(key) == True:
#             answer += "O"
#         else:
#             answer += "X"
#
#     return answer


def solution(n, k, cmd):
    alist = [i for i in range(n)]  # [0, 1, 2, ..., n-1]
    adict = dict()  # 마지막 answer를 만들 때 사용할 딕셔너리
    for i in range(n):
        adict[i] = True
    k_deleted = []  # C로 제거하는 것을 차례대로 담을 리스트

    for i in range(len(cmd)):
        order = list(cmd[i].split())
        if order[0] == "U":
            k -= int(order[1])
        elif order[0] == "D":
            k += int(order[1])
        elif order[0] == "C":
            k_deleted.append(alist[k])
            adict[alist[k]] = False
            alist = alist[:k] + alist[k + 1:]
            if k >= len(alist):
                k -= 1
        else:  # Z인 경우, 최근 것부터 복구
            # 복구 방법 틀렸다
            # :restore까지 하면 안돼
            # 복구할 값 restore보다 작은 값보다 더,
            # 큰 값보다 덜인 위치를 찾아 넣어야 한다
            restore = k_deleted.pop()
            adict[restore] = True

            if alist[k] > restore:
                j = k
                k += 1
                while j > 0:
                    j -= 1
                    if j == 0:
                        alist = [restore] + alist
                        break
                    if restore >= alist[j]:
                        alist = alist[:j + 1] + [restore] + alist[j + 1:]
                        break
            else:
                j = k
                while j < len(alist):
                    j += 1
                    if j == len(alist):
                        alist.append(restore)
                        break
                    if restore <= alist[j]:
                        alist = alist[:j] + [restore] + alist[j:]
                        break

    answer = ''

    for key in adict.keys():
        if adict.get(key):
            answer += "O"
        else:
            answer += "X"

    return answer




# n, k = 8, 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# # result = "OOOOXOOO"


n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
# result = "OOXOXOOO"

print(solution(n, k, cmd))
