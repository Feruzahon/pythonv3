'========Магические методы==========='
# магические методы- (dunder- bouble underscore) - методы- 
# это методы у которых два нижних почеркивание , 
# в начале и в конце , магия в том что мы их не вызываем напрямую, 
# они срабатывают 
# при использовании определенных символов либо функции

# _init_ -магический метод

# 10 + 3
# # 10.__add__(3)

# len('hello')
# # __len__

# # __eq__
# 10 == 4

# # __ne__
# 10 !=4

# # __lt__
# 10 < 4

# # __gt__
# 25 > 9
# # __le__
# 10 <= 11

# # __ge__
# 23 >= 34

# str()
# # __str__
# print()
# # __str__

'===================Методы====================='
# instance methods = обычные методы, которые принимают в аргументы self

# class A:
#     def func(self):
#         print('Методы обьекта',self)

# obj_a = A()
# obj_a.func()

# class methods - методы, которые принимают аргументы 
# cls (ссылка на класс). Нужно они для создания обьектов 
# или изменения атрибутов класса.Для создания класс метод 
# нужно задекорировать его в xclassmethod
# class B:
#     @classmethod
#     def func(cls):
#         print("класс метод", cls)

# cls
# class Pizza:
#     def __init__(self, radius , *ingredients):
#         self.r = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(f'готовится пицца {self.r*2}см')
#         print(f'Ингридиенты: {self.ingredients}')

#     @classmethod
#     def four_cheeze(cls, r):
#         pizza = cls(r ,"моцарелла",'дор блю','Чеддер','Голландский')
#         return pizza
    
# pizza1 = Pizza(15,'Пеперони','Моцарелла','соус')
# pizza2 = Pizza.four_cheeze(30)
# pizza3 = Pizza.four_cheeze(10)

# print(list[pizza1,pizza2,pizza3])

'static methods -прото функции внутри класса, которые'
' не работают с обьектом '
'и с классом. нужно задеркорировать в staticmethod' 

# class D:
#     @staticmethod
#     def hello(a):
#         print(a)

# obj_d= D()
# obj_d.hello('Privet')


class Cylinder:
    def __init__(self, diameter,hight):
        self.di = diameter
        self.h = hight
        self.area = self.get_area(diameter,hight)

    @staticmethod
    def get_area(di,h):
        from math import pi
        circle = pi * ( di / 2) **  2
        side = pi* di * h
        area = circle*2 + side
        return area

cylinder1 = Cylinder(4,10)
print(cylinder1.area)

cylinder2 = Cylinder(6,8)
print(cylinder2.area)