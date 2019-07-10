class TestClass:
    memberCnt = 0
    age = 10  # 클래스 변수 age

    def __init__(self, *args, **kwargs):  # 생성자 함수 정의 / name과 phone의 기본값을 주어야함
        if len(args) == 2:
            self.name = args[0]
            self.phone = args[1]
        else :
            self.name = kwargs.get("name","홍길동") #name 이 오면 주고 안넘어오면 홍길동을 주자
            self.phone = kwargs.get("phone", "010-1111")

        TestClass.memberCnt += 1 # 생성시 카운트 늘리기
        print('Instance created')

    def showInfo(self):
        return str(self)  # str함수 부르기
        # return self.__str__()

    def __str__(self):  # 인스턴스 값이 보였으면 하는 형변환
        return "name:{0} phone:{1} age:{2}".format(self.name, self.phone, self.age)
        # 소수점 표현 {0(인덱스순서):6(6자리중에서).3f(소수셋째자리까지)}

    def __del__(self):  # 인스턴스 값 삭제
        TestClass.memberCnt -= 1 #삭제시 카운트 --
        print('Instance removed')


print(TestClass.age)
t1 = TestClass()
t2 = TestClass('홍길동', '010-1111-1111')
t3 = TestClass(name = '김개동', phone = '090-111') #딕셔너리로
print(id(t1), t1.__dict__)
print(id(t2), t2.__dict__)
print(t1.showInfo())
print(str(t2))

print(TestClass.memberCnt)

t2.age = 25
print(id(t2), t2.__dict__)
print(str(t2))
del t2
print(TestClass.memberCnt)
print('end')
