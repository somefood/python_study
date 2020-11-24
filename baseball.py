"""숫자 야구게임
   version 2.0
"""

import random

# 상수 설정
SCORE_START = 1000
SCORE_TRY = -100
SCORE_STRIKE = 30
SCORE_BALL = 20
SCORE_NOTHING = 50
TRY_MAX = 10


def get_hidden_number():
    """ 서로 다른 숫자로 이루어진 3자리 난수열 생성 """
    items = random.sample(range(1, 10), 3)
    hidden = [str(x) for x in items]
    return hidden


def get_my_number():
    """ 숫자입력과 적절성 검토
    적절성 검토를 위해 내부적으로 is_valid_input() 함수를 호출한다.
    """
    flag = False
    while flag is False:
        data = input('숫자를 입력하세요 : ')
        flag = is_valid_input(data)
    return data


def is_valid_input(data):
    # 입력값이 숫자인가?
    if not (data.isdecimal()):
        print('[{this}]은(는) 숫자가 아닙니다!'.format(this=data))
        return False
    # 입력된 숫자가 3자리인가?
    elif len(data) != 3:
        print('[%s]은(는) %d자리입니다! 세자리 수를 입력하세요' % (data, len(data)))
        return False
    # 입력된 숫자열에 같은 수가 있는가?
    elif (data[0] == data[1] or data[0] == data[2] or data[1] == data[2]):
        print('같은 숫자쌍이 있습니다! 각 자리의 숫자는 서로 달라야합니다.')
        return False
    else:
        return True


def get_ballcount(hidden, data):
    """ 볼카운트를 계산하여 튜플 자료형으로 반환한다. """
    strikes = 0
    balls = 0
    for n, value1 in enumerate(hidden):
        for m, value2 in enumerate(data):
            if value1 == value2:
                if n == m:
                    strikes += 1
                else :
                    balls += 1
    return (strikes, balls)


def update_score(strikes, balls, score):
    """ 시도횟수와 볼카운트를 참조하여 갱신됨 점수를 반환한다. """
    score += SCORE_TRY
    if strikes == 0 and balls == 0:
        score += SCORE_NOTHING
    else:
        score += strikes*SCORE_STRIKE + balls*SCORE_BALL
    return score


def show_result(trys, strikes, balls, score):
    """ 결과 출력 (볼카운트, 점수) """
    if strikes == 0 and balls == 0:
        print('=> [%2d]차 시도, 낫싱입니다. %5d점' % (trys, score))
    else:
        print('=> [%2d]차 시도, %d 스트라이크 %d 볼입니다. %5d점' % (trys, strikes, balls, score))


def you_succeeded(trys, score):
    """ 게임 승리 메시지 출력 """
    print('\n축하합니다!')
    print('{number}회 시도만에 성공했네요'.format(number=trys))
    print('당신의 최종 점수는 %d점입니다.' % score)


def you_failed(hidden, score):
    """ 게임 패배 메시지 출력 """
    print('\n안타깝네요!')
    print('숨겨진 수는 %s입니다.' % hidden)
    print('당신의 최종 점수는 %d점입니다.' % score)


print('--------------------------')
print(' 숫자 야구 게임 ver. 2.0 ')
print('--------------------------')

# 서로 다른 숫자로 이루어지 3자리 난수열 생성
hidden = get_hidden_number()

trys = 1
score = SCORE_START

while True:

    my_number = get_my_number()
    strikes, balls = get_ballcount(hidden, my_number)
    score = update_score(strikes, balls, score)
    show_result(trys, strikes, balls, score)

    if strikes == 3:
        you_succeeded(trys, score)
        break
    if trys > TRY_MAX or score <= 0:
        you_failed(score, hidden)
        break

    trys += 1