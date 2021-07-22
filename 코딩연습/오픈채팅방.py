def solution(record):
    answer = []
    enter_m = "님이 들어왔습니다."
    exit_m = "님이 나갔습니다."
    logindex = dict()
    usernick = dict()
    idx = 0
    for timeline in record:
        pack = list(timeline.split())   # 행동, uid, 닉네임
        if pack[0] == "Enter":
            if logindex.get(pack[1]):
                prenick = usernick.get(pack[1])
                if not pack[2] == prenick:
                    for now in logindex.get(pack[1]):
                        answer[now] = answer[now].replace(prenick, pack[2])
                    usernick[pack[1]] = pack[2]
                logindex[pack[1]].append(idx)
            else:
                usernick[pack[1]] = pack[2]
                logindex[pack[1]] = [idx]
            answer.append(pack[2] + enter_m)
            idx += 1
        elif pack[0] == "Change":
            if logindex.get(pack[1]):
                prenick = usernick.get(pack[1])
                if not pack[2] == prenick:
                    for now in logindex.get(pack[1]):
                        answer[now] = answer[now].replace(prenick, pack[2])
                    usernick[pack[1]] = pack[2]
        else:
            logindex[pack[1]].append(idx)
            answer.append(usernick.get(pack[1]) + exit_m)
            idx += 1

    return answer