import random

SCORE_START = 1000
SCORE_TRY = -100
SCORE_STRIKE = 100
SCORE_BALL = 50
SCORE_NOTHING = 150
TRY_MAX = 10

print('-' * 14)
print('숫자 야구 게임')
print('-' * 14)

items = random.sample(range(1, 10), 3)
hidden = [str(x) for x in items]

ntry = 1
score = SCORE_START
while True:

    while True:
        data = input('숫자를 입력하세요 : ')
        if not (data.isdecimal()):
            print('[{this}]은(는) 숫자가 아닙니다!'.format(this=data))
        elif not (len(data) is 3):
            print('[%s]은(는) $d자리입니다! 세자리 수를 입력하세요.' % (data, len(data)))
        elif (data[0] == data[1] or data[0] == data[2] or data[1] == data[2]):
            print('같은 숫자쌍이 있습니다! 각 자리의 숫자를 서로 다르게 하십시오.')
        else:
            break

    nstrike = 0
    nball = 0
    for n, hvalue in enumerate(hidden):
        for m, value in enumerate(data):
            if hvalue == value:
                if n == m:
                    nstrike += 1
                else:
                    nball += 1

    score += SCORE_TRY
    if nstrike is 0 and nball is 0:
        score += SCORE_NOTHING
    else:
        score += nstrike*SCORE_STRIKE + nball*SCORE_BALL

    if nstrike is 0 and nball is 0:
        print('=> [%2d]차 시도, 낫싱입니다. %5d점' % (ntry, score))
    else:
        print('=> [%2d]차 시도, %d 스트라이크 %d 볼입니다. %5d점' % (ntry, nstrike, nball, score))

        # 게임종료 여부 확인
    if nstrike is 3:
        print('축하합니다!')
        print('{number}회 시도만에 성공했네요'.format(number=ntry))
        print('당신의 점수는 %d점입니다.' % score)
        break
    if ntry > TRY_MAX or score <= 0:
        print('안타깝네요!')
        print('숨겨진 수는 %s입니다.' % hidden)
        print('당신의 최종 점수는 %d점입니다.' % score)
        break
    ntry += 1



