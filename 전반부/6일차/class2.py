class My:
    def __init__(self):
        self.name = 'python'
        print('My')

    def getName(self):
        return self.name

class SubMy(My):
    def __init__(self):
        super().__init__() #이걸 해 주어야 합니다
        print('SubMy')


#
# m1 = My()
# print(m1.getName())

cm1 = SubMy()
print(cm1.getName())