class PropertyClass:
    def __init__(self, tmp = -2, ref = 2):
        if tmp > 0: tmp = -2
        if ref < 0 : ref = 2
        self.__tmp = tmp
        self.__ref = ref

    @property
    def tmp(self):
        return self.__tmp

    @tmp.setter
    def tmp(self, val):
        if val < 0:
            self.__tmp = val
        else:
            self.__tmp = -2

    @property
    def ref(self):
        return self.__ref

    @ref.setter
    def ref(self , val):
        if 1< val < 5:
            self.__ref = val
        else:
            self.__ref = 2

    def showInfo(self):
        return '냉동실 온도는 {0} 도, 냉장실 온도는 {1} 도 입니다'.format(self.__tmp,self.__ref)

    @classmethod
    def sampleClassMethod(cls):
        return 'ClassMethod'
    @staticmethod #클래스 매써드랑 차이가 없다
    def sampleStaticMethod():
        return 'StaticMethod'

t1 = PropertyClass()

print(t1.showInfo())
t1.tmp = 10
print(t1.showInfo())


t1.tmp = -5
print(t1.showInfo())

t1.ref = 4
print(t1.showInfo())

t1.ref = -4
print(t1.showInfo())

#클래스 매서드는 클래스 이름으로 호출해라
print(PropertyClass.sampleClassMethod())
print(t1.sampleClassMethod()) #인스턴스로 불러도 호출됨

print(PropertyClass.sampleStaticMethod())
print(t1.sampleStaticMethod())