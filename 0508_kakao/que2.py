movement = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # 상 하 좌 우 / 즉 [x, y]
N = 5


def isDistance(place):
    for y in range(N):
        for x in range(N):
            if place[y][x] == "P":  # (0, 0)부터 (4, 4)까지 순회하는데, P인 경우 거리두기 검증
                for move in movement:
                    nx, ny = x + move[0], y + move[1]
                    if -1 < nx < N and -1 < ny < N:
                        if place[ny][nx] == "P":  # 바로 옆자리가 P면 거리두기 실패
                            return 0
                        elif place[ny][nx] == "O":  # 바로 옆자리가 테이블이면 확인이 필요
                            for n_move in movement:
                                nnx, nny = nx + n_move[0], ny + n_move[1]
                                if -1 < nnx < N and -1 < nny < N and not (x == nnx and y == nny):
                                    if place[nny][nnx] == "P":
                                        return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(isDistance(place))  # 거리두기 못하면 중간에 0 반환

    return answer



places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))