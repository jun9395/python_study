# # dfs?
# def find_root(goal, cost):
#
#
# # goal로 다이렉트로 오는 경로를 찾자
# # road_dict[goal][0]에 roads의 i가 담겨있다
# # 즉 roads[i][0]까지 가는 경로를 찾으면 된다
# # 만약 현재 goal이 trap이라면,
#
#
# def solution(n, start, end, roads, traps):
#     road_dict = dict()
#     # [[참고할 roads의 i번호], [참고할 roads의 i번호]] 형태
#     # road_dict[key][0]은 key로 오는 경우를 참고할 수 있는 roads의 i
#     # road_dict[key][1]은 key에서 가는 경우를 참고할 수 있는 roads의 i
#     for i in range(len(roads)):
#         if road_dict.get(roads[i][0]):
#             road_dict[roads[i][0]][1].append(i)
#         else:
#             road_dict[roads[i][0]] = [[], [i]]
#         if road_dict.get(roads[i][1]):
#             road_dict[roads[i][1]][0].append(i)
#         else:
#             road_dict[roads[i][1]] = [[i], []]
#
#     trap_dict = dict()  # trap_dict.get(노드) 해서 True면 함정
#     for trap in traps:
#         trap_dict[trap] = True
#
#     find_root(end, 0)  # 현재 코스트는 0인 상태로, end로 도달하기 위한 경로를 찾자
#
#     answer = 0
#     return answer
#
#
#
#
#
# # node_dict = dict()
# #     # [pre_nodes, next_nodes, pre_costs, next_costs]
# #     for road in roads:
# #         if node_dict.get(road[0]):
# #             node_dict[road[0]][1].append(road[1])
# #             node_dict[road[0]][3].append(road[2])
# #         else:
# #             node_dict[road[0]] = [[], [road[1]], [], [road[2]]]
# #         if node_dict.get(road[1]):
# #             node_dict[road[1]][0].append(road[0])
# #             node_dict[road[1]][2].append(road[2])
# #         else:
# #             node_dict[road[1]] = [[road[0]], [], [road[2]], []]


# dfs?

def solution(n, start, end, roads, traps):
    result = [9999999]
    trap_dict = dict()  # trap_dict.get(노드) 해서 True면 함정
    for trap in traps:
        trap_dict[trap] = True

    road_dict = dict()
    for road in roads:
        if road_dict.get(road[0]):
            road_dict[road[0]][1][road[1]] = road[2]
        else:
            road_dict[road[0]] = [dict(), {road[1]: road[2]}]

        if road_dict.get(road[1]):
            road_dict[road[1]][0][road[0]] = road[2]
        else:
            road_dict[road[1]] = [{road[0]: road[2]}, dict()]

    def find_root(node, cost):
        if node == end:
            if result[0] > cost:
                result[0] = cost
            return

        # node가 trap이라면
        if trap_dict.get(node):
            # road_dict[node][0]의 key들을 순회하면서
            key_set = [x for x in road_dict[node][0].keys()]
            for key in key_set:
                # road_dict[key][1]에 있는 .get(node)를 road_dict[key][0][node] = .get(node) 하고
                road_dict[key][0][node] = road_dict[key][1].get(node)
                # del road_dict[key][1][node] 한다
                del road_dict[key][1][node]

            key_set = [x for x in road_dict[node][1].keys()]
            for key in key_set:
                road_dict[key][1][node] = road_dict[key][0].get(node)
                del road_dict[key][0][node]
            # road_dict[node]의 [0]과 [1]을 바꿔준다
            road_dict[node][0], road_dict[node][1] = road_dict[node][1], road_dict[node][0]

        # node에서 나가는 길을 찾자
        # road_dict[node][1]에 dict 형태로 있다
        # 그 dict 안의 key를 한번씩 find_root(key, value) 한다
        for next_node in road_dict[node][1].keys():
            find_root(next_node, cost + road_dict[node][1][next_node])

    find_root(start, 0)  # 현재 코스트는 0인 상태로, end로 도달하기 위한 경로를 찾자

    answer = 0
    return answer


n, start, end = 3, 1, 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]

print(solution(n, start, end, roads, traps))