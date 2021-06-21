# 각각의 이름은 3개의 파츠로 되어있다. 영어 알파벳만 있다
# 이름, 미들네임, 성
# 스페이스바로 구분된다
# First.Last@Company.com
# 단, Last는 최대 8개까지만
# 소문자로 구성되고, 하이픈은 없어야 한다
# 하이픈은 Last 8까지 줄이기 전에 제거하고 시작해야 한다
# 추가적으로, 같은 이메일을 갖는 사람이 1명보다 많다면
# @ 앞에 숫자를 붙여서 구분하라
# jd@company.com, jd2@company.com, jd3@company.com, ...
# string S는 ;로 사람 이름을 구분해서 준다
# "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; ..."
# C는 컴패니다

# N은 3부터 1000까지의 정수
# M은 1부터 100까지의 정수
# S는 오로지 a-z 또는 A-Z, 스페이스, 하이픈과 세미콜론으로만 이루어져 있다
# string S contains valid names; no name appears more than once
# = 중복이름 없다
# C는 a-z 또는 A-Z으로만 이루어져 있다

# 이름1 <이메일1>; 이름2 <이메일2>; ... 을 출력하라
# 정확성에 집중해서 풀라. 효율성은 차후 생각하라

def solution(S, C):
    emails = dict()

    answer = ''
    names = S.split("; ")
    company = "@" + C.lower() + ".com"

    for name in names:
        sepa_name = list(name.lower().split())
        if len(sepa_name) > 2:
            sepa_name = sepa_name[:1] + sepa_name[2:]
        first = sepa_name[0]
        last = sepa_name[1]
        last = last.replace('-', '')
        email = first + '.' + last[:8] + company
        if emails.get(email):
            emails[email] += 1
            email = first + '.' + last[:8] + str(emails[email]) + company
        else:
            emails[email] = 1

        if answer == '':
            answer = name + " <" + email + ">"
        else:
            answer += "; " + name + " <" + email + ">"

    return answer


S = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
C = "example"

print(solution(S, C))