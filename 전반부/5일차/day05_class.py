# 클래스
# class 클래스명대문자(부모클래스)
# 인스턴스 == 객체
# 객체(Object) = 속성(Attribute) + 기능(Method)

class Square:
    alpha = 5
    def __init__(self,width = 0,height= 0) : #self 는 빼고 계산, 클래스에서 정의된 변수
        self.width = width
        self.height = height #인스턴스 멤버 변수
        self.__pwidth = width #바깥에서 접근 못하게
        self.__pheight = height #private __
        self._ptheight = height #protected _

    def calcArea(self):
        return self.height * self.width

    def test(self):
        return self.__pheight*self.__pwidth
    def get_second(self):
        return self.__second
    def set_second(self, value):
        self.__second = value



print(type(Square))

sq0 = Square()
sq1 = Square(5, 10) #Square 타입의 객체를 sq1로 생성
sq2 = Square(6, 20)
sq2.width = 30
sq2.height = 30
sq2.__pwidth = 10
sq2.__pheight = 10
print(Square.calcArea(sq2)) #클래스 이름으로 호출
print(Square.test(sq2)) #밖에서 주면 안바뀜

sq0.alpha = 44
print(sq1.alpha)
print(sq0.alpha)

a = Square(5,7)
print(a.get_second, a.height)
# sq1.__init__() #생성자
# sq1.__delattr__() #소멸자
# sq1.__dict__ #경로

# self : 인스턴스 변수, 인스턴스 매써드

#속성 @property --> private 변수를 만들 었을 때 씀 ///////get
# @price.setter ////////set

# @property
# def price(self):
#   return self_price
# @price.setter
# def price(self, value):
#   self_price = value

# def get_price(self):
#   return self_price
# def set_price(self,value):
#   self_price = value

#price = property(get_price, set_price)

#다중상속
# class 클래스이름(부모클래스1, 부모클래스2)