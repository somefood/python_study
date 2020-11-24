"""숫자 야구게임
   version 1.0f
"""

import random

# 상수 설정
SCORE_START = 1000
SCORE_TRY = -100
SCORE_STRIKE = 30
SCORE_BALL = 20
SCORE_NOTHING = 50
TRY_MAX = 10

print('--------------------------')
print(' 숫자 야구 게임 ver. 1.0f ')
print('--------------------------')

# 서로 다른 숫자로 이루어지 3자리 난수열 생성
items = random.sample(range(1,10), 3)
hidden = [str(x) for x in items]

n_try = 1
score = SCORE_START

while True:

    # 숫자입력
    while True:

        data = input('숫자를 입력하세요 : ')

        # 입력값이 숫자인가?
        if not (data.isdecimal()):
            print('[{this}]은(는) 숫자가 아닙니다!'.format(this=data))

        # 입력된 숫자가 3자리인가?
        elif len(data) is not 3:
            print('[%s]은(는) %d자리입니다! 세자리 수를 입력하세요' % (data, len(data)))

        # 입력된 숫자열에 같은 수가 있는가?
        elif (data[0] == data[1] or data[0] == data[2] or data[1] == data[2]):
            print('같은 숫자쌍이 있습니다! 각 자리의 숫자는 서로 달라야합니다.')

        else:
            break

    # 볼카운트 계산
    n_strike = 0
    n_ball = 0
    for n, value1 in enumerate(hidden):
        for m, value2 in enumerate(data):
            if value1 == value2:
                if n == m:
                    n_strike += 1
                else :
                    n_ball += 1

    # 점수 계산
    score += SCORE_TRY
    if n_strike is 0 and n_ball is 0:
        score += SCORE_NOTHING
    else:
        score += n_strike*SCORE_STRIKE + n_ball*SCORE_BALL

    # 볼카운트와 점수 출력
    if n_strike is 0 and n_ball is 0:
        print('=> [%2d]차 시도, 낫싱입니다. %5d점' % (n_try, score))
    else:
        print('=> [%2d]차 시도, %d 스트라이크 %d 볼입니다. %5d점' % (n_try, n_strike, n_ball, score))

    # 게임종료 여부 확인
    if n_strike is 3:
        print('\n 축하합니다!')
        print('{number}회 시도만에 성공했네요'.format(number=n_try))
        print('당신의 점수는 %d점입니다.' % score)
        break
    if n_try > TRY_MAX or score <= 0:
        print('\n 안타깝네요!')
        print('숨겨진 수는 %s입니다.' % hidden)
        print('당신의 최종 점수는 %d점입니다.' % score)
        break
    n_try += 1