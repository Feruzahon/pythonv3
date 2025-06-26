# '==================OOP=================='
# # OOP - Object-orientated programing
# # ООП - Обьектно ориентированное программирование (парадигма)


# a = 312
# def func():
#     ...

# class Person:
#     # перменные внутри класса, называются аттрибутами (если переменная рядом с классом, то их значения будут у всех обьектов)
#     arms = 2 
#     legs = 2

#     # функция внутри класса, называется методом
#     def __init__(self, n, a):
#         # __init__ - метод, который добавляет в обьект те аттрибуты, которые у обьектов разные
#         # self - это ссылка на обьект, который только что создался 
#         self.name = n
#         self.age = a

#     def fly(self):
#         print(f'Я - {self.name}, могу летать')



# obj1 = Person('Katana', 21)
# obj2 = Person('Nick', 21)

# # print(obj1.arms, obj1.legs, obj1.name, obj1.age)
# # 2, 2, katana, 21

# # print(obj2.arms, obj2.legs, obj2.name, obj2.age)
# # 2, 2, nick, 21

# obj1.fly()
# obj2.fly()

# '==========================Обьекты класса=============='
# # обьект, экпземпляр, instance класса - конечный продукт, созданные по шаблону (классу)

# '====================Аттрибуты и методы==============='
# # аттрибуты - переменые
# # методы - функции

# class A:
#     var1 = 'переменная класса'

#     def __init__(self):
#         self.var2 = 'переменная обьекта'

#     def func(self):
#         return 'метод'
    


# class House:
#     smart_ = True 
#     class_ = 'comfort+'

#     def __init__(self, color, room_count):
#         self.color = color
#         self.room_count = room_count

#     def action(a):
#         if a == '2 раза хлопнул':
#             print('свет включен')
#         elif a == 'крикнул':
#             print('звонок в спец.службу')

# h1 = House('green', 10)
# h2 = House('red', 15)

# # __new__ - это метод, который создает пустой обьект (оболочка)
# # __init__ - это метод, который после создания засунет туда переменные (этот процесс называется инициализацией)


# '=====================Принципы ООП==================='
# # Наследование
# # Инкапсуляция
# # Полиморфизм
# # Абстракция
# # Ассоциация (Композиция, Агрегация)


# # Напишите калькулятор на классе с методами add, percent, sqrt



# class Calc:
#     def add(self, num1, num2):
#         print(num1+num2)

#     def sqrt(self, num1):
#         print(num1 ** 0.5)

#     def precent(self, num1, prec):
#         print((num1 * prec) / 100) 

# calc = Calc()
# calc.add(10, 56)
# calc.sqrt(81)
# calc.precent(90, 90)

# calc2 = Calc()


# # Наследование 


class A:
    var = 1

# class B:
#     ...

# class C(A, B):
#     ...

# obj_c = C()
# print(obj_c.var)
# print(C.mro())
# # mro (method resolution order) - порядок поиска аттрибутов

# '----------Проблемы множественного наследования-------'
# # Проблема ромба (решена при помощи mro)

# # class A:
# #     ...

# # class B:
# #     ...

# # class C(A, B):
# #     ...

# # obj_c = C()
# # print(obj_c.var)

# # Проблема перекрестного наследования (не решенная)
# # class A:
# #     ...

# # class B:
# #     ...

# # class D(A, B):
# #     ...

# # class E(B, A):
# #     ...

# # class F(D, E):
# #     ...



# # super() - функция для обращения к род.классу



# # Используя super(), реализуйте классы A, B(A), C(B), в каждом определите метод
# # describe(), который вызывает аналогичный метод родителя. Проверьте порядок
# # вызовов.



# class A:
#     def describe(self):
#         print('A')


# class B(A):
#     def describe(self):
#         super().describe()

# class C(B):
#     def describe(self):
#         super().describe()


# obj_c = C()
# obj_c.describe()


# 10. (Дополнительное задание) Создайте структуру классов для зоопарка: класс
# Animal, от которого наследуются Mammal и Bird. Создайте классы Bat и Penguin,
# которые наследуют от соответствующих классов. Реализуйте методы,
# отображающие особенности каждого животного. Используйте super() и
# множественное наследование, где необходимо.


class Animal:
    ...

class Mammal(Animal):
    a = 'питание молоком'

class Bird(Animal):
    a = 'издают звуки'

class Bat(Mammal):
    def action(self):
        print(super().a)
        print('эхолокация')


class Penguin(Bird):
    def action(self):
        print(super().a)
        print('умеет плавать')


'=============================Миксины=============================='
# Миксины - это классы помощники, от них наследуются чтобы расширить функционал другого класса. От миксинов не создаются обьекты

class FlyMixin:
    def fly(self):
        print('умею летать')

class WalkMixin:
    def walk(self):
        print('умею ходить')

class SwimMixin:
    def swim(self):
        print('умею плавать')


class Cat(WalkMixin, SwimMixin):
    name = 'кошка'
    def hunt(self):
        print('умею охотиться')


class Human(WalkMixin, SwimMixin):
    name = 'человек'
    def talk(self):
        print('умею говорить')


class Duck(FlyMixin, SwimMixin, WalkMixin):
    name = 'утка'
    def talk(self):
        print('умею крякать')




obj_human = Human()
print(obj_human.name)
print(obj_human.swim())
print(obj_human.walk())
print(obj_human.talk())
obj_cat = Cat()
print(obj_cat.name)
print(obj_cat.swim())
print(obj_cat.walk())
print(obj_cat.hunt())
obj_duck = Duck
print(obj_duck.name)
print(obj_duck.swim())
print(obj_duck.walk())
print(obj_duck.hunt())
print(obj_duck.fly())



objects = [Cat(), Duck(), Human()]
for obj in objects:
    print(obj.name)
    attrs = ['fly', 'swim', 'talk', 'walk', 'hunt']
    for attr in attrs:
        if hasattr(obj, attr):
            method = getattr(obj, attr)
            method()