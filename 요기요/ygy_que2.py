# 파일의 세부리스트가 있는 string을 받는다
# 이 파일이 갖고 있는 서브셋에서 쿼리 계산을 해라
# 아스키코드10으로 구분된 N줄의 string이 있다
# 각 라인은 하나의 파일의 정보를 갖고 있고,
# 순서대로 size, date, name로 그룹되어 있다
# 이들은 길이가 정해져있고 스페이스로 구분되어 있다
# 다음 예시를 보라
# size는 길이가 5이고 사이즈는 사람이 읽을 수 있는 포맷이다.
# 사이즈는 K, M, G 중의 하나
# 7M이라고 하면, 7 * 2^20 bytes
# date는 길이가 10이고 yyyy-mm-dd 형태로 주어진다
# name은 최대 255개 이하의 출력 가능한 아스키코드이다
# 적어도 1개의 '.'을 갖고, '.' 이후는 확장자라고 한다

# 다음과 같은 파일의 갯수를 세라
# 백업 파일일 것. ~로 끝나는 파일을 백업이라고 한다
# 사이즈가 14M 이하일 것
# 1990-01-31 이후에 수정됐을 것

def solution(S):
    files = list(S.split("\n "))
    answer = 0

    for file in files:
        size, date, name = file.strip().split(' ')
        flag = 0
        # 이름의 끝이 ~, 즉 백업파일이다
        if name[-1] == '~':
            # 사이즈가 14M 이하이다
            if ord('0') <= ord(size[-1]) <= ord('9'):
                flag = 1
            elif size[-1] == 'K' or size[-1] == 'k':
                flag = 1
            elif size[-1] == 'M' or size[-1] == 'm':
                if int(size[:len(size) - 1]) <= 14:
                    flag = 1
        if flag:
            year, month, day = map(int, date.split('-'))
            if year > 1990:
                answer += 1
            else:
                if month > 1:
                    answer += 1
                else:
                    if day >= 31:
                        answer += 1
    return answer

S = ' 715K 2009-09-23 system.zip~\n 179K 2013-08-14 to-do-list.xml~\n 645K 2013-06-19 blockbuster.mpeg~\n  536 2010-12-12 notes.html\n 688M 1990-02-11 delete-this.zip~\n  23K 1987-05-24 setup.png~\n 616M 1965-06-06 important.html\n  14M 1992-05-31 crucial-module.java~\n 192K 1990-01-31 very-long-filename.dll~'

print(solution(S))