def solution(genres, plays):
    answer = []
    n = len(genres)
    
    genre_played = dict()
    maniest = dict()
    
    for i in range(n):
        if genre_played.get(genres[i]):
            genre_played[genres[i]] += plays[i]
            if len(maniest[genres[i]]) == 1:
                if plays[i] > plays[maniest[genres[i]][0]]:
                    maniest[genres[i]] = [i, maniest[genres[i]][0]]
                elif plays[maniest[genres[i]][0]] > plays[i]:
                    maniest[genres[i]].append(i)
                else:
                    if i < maniest[genres[i]][0]:
                        maniest[genres[i]].append(i)
                    else:
                        maniest[genres[i]] = [i, maniest[genres[i]][0]]
            else:
                if plays[maniest[genres[i]][1]] > plays[i]:
                    continue
                elif plays[i] == plays[maniest[genres[i]][1]]:
                    if i < maniest[genres[i]][1]:
                        maniest[genres[i]][1] = i
                elif plays[maniest[genres[i]][0]] > plays[i] > plays[maniest[genres[i]][1]]:
                    maniest[genres[i]][1] = i
                elif plays[maniest[genres[i]][0]] == plays[i]:
                    if maniest[genres[i]][0] > i:
                        maniest[genres[i]][0], maniest[genres[i]][1] = i, maniest[genres[i]][0]
                    else:
                        maniest[genres[i]][1] = i
                else:
                    maniest[genres[i]][0], maniest[genres[i]][1] = i, maniest[genres[i]][0]
        else:
            genre_played[genres[i]] = plays[i]
            maniest[genres[i]] = [i]

    temp = []
    for key, value in genre_played.items():
        temp.append([value, key])
    temp.sort(reverse=True)

    for keys in temp:
        answer.extend(maniest[keys[1]])

    return answer