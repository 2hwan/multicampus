class FourCalc :

    def __init__(self, num1 = None, num2 = None):
        self.first = num1
        self.second = num2

    def add(self) :
        return self.first + self.second

    def sub(self) :
        return self.first - self.second

    def mul(self) :
        return self.first * self.second

    def div(self) :
        return self.first / self.second

class MoreFourCalc(FourCalc) :
    add_num = 10

    @classmethod
    def setPI(cls):
        pass

    @staticmethod
    def setPI():
        pass

    def pow(self):
        return self.first**self.second

    def div(self) :
        if self.second == 0:
            return 0
        else : return self.first / self.second


if __name__ == "__main__" : #이 자체를 실행한 경우만 들어감, 다른데서 import할 때는 실행 안 됨
    a = FourCalc(5, 7)
    print(a.add(), a.sub(), a.mul(), a.div())

    b = FourCalc(10, 5)
    print(b.add(), b.sub(), b.mul(), b.div())

    # c = FourCalc(5, 0)
    # print(c.div())
    #
    ch_a = MoreFourCalc(10, 2)
    print(ch_a.add(), ch_a.sub(), ch_a.mul())
    print(ch_a.div(), ch_a.pow())

    ch_b = MoreFourCalc(8, 2)
    print(MoreFourCalc.add_num,id(MoreFourCalc.add_num))
    print(ch_a.add_num,id(ch_a.add_num))
    print(ch_b.add_num, id(ch_b.add_num))

    #MoreFourCalc.add_num = 20
    ch_a.add_num = 20 # 객체 명으로 클래스 접근 x
    print(MoreFourCalc.add_num,id(MoreFourCalc.add_num))
    print(ch_a.add_num,id(ch_a.add_num))
    print(ch_b.add_num, id(ch_b.add_num))