from collections import deque


def solution(n, vertex):
    mapping = dict()
    max_node = 0

    for edges in vertex:
        if mapping.get(edges[0]):
            mapping[edges[0]].append(edges[1])
        else:
            mapping[edges[0]] = [edges[1]]
        if mapping.get(edges[1]):
            mapping[edges[1]].append(edges[0])
        else:
            mapping[edges[1]] = [edges[0]]
        if max_node < edges[0]:
            max_node = edges[0]
        if max_node < edges[1]:
            max_node = edges[1]

    short_ways = [max_node] * (max_node + 1)
    stack = deque()
    stack.append([1, 0])
    while stack:
        node, edge = stack.popleft()
        if short_ways[node] > edge:
            short_ways[node] = edge
            for next_p in mapping[node]:
                stack.append([next_p, edge + 1])

    answer = []
    max_length = 0
    for idx in range(2, max_node + 1):
        if max_length < short_ways[idx]:
            max_length = short_ways[idx]
            answer = [idx]
        elif max_length == short_ways[idx]:
            answer.append(idx)

    return len(answer)
