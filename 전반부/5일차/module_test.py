from fourcalc import FourCalc, MoreFourCalc #from 모듈 import 클래스이름

c1 = FourCalc(6.3)
print(c1.add())

print('c1', isinstance(c1, FourCalc))

ch_a = MoreFourCalc(10, 2)
print(ch_a.add(), ch_a.sub(), ch_a.mul())
print(ch_a.div(), ch_a.pow())

print('ch_a_자식', isinstance(ch_a, MoreFourCalc)) # 자식 --> 부모 가능
print('ch_a_부모', isinstance(ch_a, FourCalc))     # 자식 --> 자식 불가능
print('c1_자식', isinstance(c1, MoreFourCalc))     # 부모 --> 자식 불가능
# 다중상속, 인터페이스 없다