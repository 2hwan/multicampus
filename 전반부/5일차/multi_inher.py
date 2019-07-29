class Car:
    '''Parent Class'''
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show" Method!'

class BmwCar(Car):
    '''Sub Class'''
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name

class BenzCar(Car):
    '''Sub Class'''
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show(self): # Override
        super().show()
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name

model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)
print(model1.type)
print(model1.car_name)
print(model1.show())
print(model1.show_model())

# Method Overriding
model2 = BenzCar('220d', 'suv', 'black')
print(model2.show())

#Parent Method Call
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())

#Inheritance Info
print('Inheritance Info : ', BmwCar.mro())
print('Inheritance Info : ', BenzCar.mro())

