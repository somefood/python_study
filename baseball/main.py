"""숫자 야구게임 클래스 활용
   version 3.0
"""

import baseball

# 상수
SCORE_START = 1000
SCORE_TRY = -100
SCORE_STRIKE = 30
SCORE_BALL = 20
SCORE_NOTHING = 50
TRY_MAX = 10


def get_my_number():
    """ 숫자입력과 적절성 검토
    적절성 검토를 위해 내부적으로 Baseball.is_valid_input() 메서드를 호출한다.
    """
    flag = False
    while flag is False:
        data = input('숫자를 입력하세요 : ')
        (flag, message) = baseball.is_valid_input(data)
        if flag is False:
            print(message)
    return data


def update_score(strikes, balls, score):
    """ 시도횟수와 볼카운트를 참조하여 갱신된 점수를 반환한다. """
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


#
#  메인 코드
#

print('-----------------------')
print(' 숫자야구게임 ver. 3.0 ')
print('-----------------------')

# base = Baseball()
hidden = baseball.get_hidden_number()  # 숨겨진 수 만들기

trys = 1
score = SCORE_START

# 메인루프 실행
while True:

    my_number = get_my_number()  # 키보드로부터 숫자를 입력받는다.
    (strikes, balls) = baseball.get_ballcount(hidden, my_number)
    score = update_score(strikes, balls, score)
    show_result(trys, strikes, balls, score)

    # 게임 종료 조건
    if strikes == 3:
        you_succeeded(trys, score)
        break
    if trys > TRY_MAX or score <= 0:
        you_failed(score, hidden)
        break

    trys += 1