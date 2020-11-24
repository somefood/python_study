""" 숫자야구게임 클래스
버전 1.0

공용메서드
value = get_hidden_number(): 서로 다른 숫자로 이루어진 3자리 난수열 반환
flag,message = is_valid_input(value): 인자 value가 적절한 숫자 데이터이면 True를
    그렇지않으면, False와 해당 오류메시지를 튜플로 반환
ns, nb = get_ballcount(value1, value2): 두 인자 value1과 value2의 각 자리수 숫자를
        비교해서 볼카운트를 튜플로 반환
"""

import random


class Baseball():

    def get_hidden_number(self):
        """ 서로 다른 숫자로 이루어진 3자리 난수열 생성 """
        items = random.sample(range(1, 10), 3)
        hidden = [str(x) for x in items]
        return hidden

    def is_valid_input(self, data):
        """ flag, message = Baseball.is_valid_input(data)
        인자 data가 적절한 숫자 데이터이면 True를,
        그렇지 않으면 False와 해당하는 오류 메시지를 튜플 자료형으로 반환한다.
        """
        flag = True
        message = []

        if not(data.isdecimal()):
            flag = False
            message = '[{this}]은(는) 숫자가 아닙니다!'.format(this=data)

        elif len(data) != 3:
            flag = False
            message = "{}은(는) {}자리입니다! 세자리 수를 입력하세요.".format(data, len(data))

        elif data[0] == data[1] or data[0] == data[2] or data[1] == data[2]:
            flag = False
            message = '같은 숫자쌍이 있습니다! 각 자리의 숫자는 서로 달라야합니다.'

        return flag, message

    def get_ballcount(self, hidden, data):
        strikes, balls = 0, 0
        for n, hvalue in enumerate(hidden):
            for m, mvalue in enumerate(data):
                if hvalue == mvalue:
                    if n == m:
                        strikes += 1
                    else:
                        balls += 1

        return (strikes, balls)


# 모듈로 불러와도 실행되니까 이런식으로 해서 메소드 형태로 사용한다! (신기하다)
_inst = Baseball()
get_hidden_number = _inst.get_hidden_number
is_valid_input = _inst.is_valid_input
get_ballcount = _inst.get_ballcount