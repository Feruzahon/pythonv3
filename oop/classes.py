# '============ OOP ========================='
# # OOP-
# # ООП-Обьектно ориентированная программировани(парадигма)
class Person:
    arms =2
    legs =2

    def __init__(self,n ,a):
        self.name = n
        self.age =a
# '=====Обьект класса========'
# # обьект, экземплярами? instance класс -конечный продукт, 
# # созданные по шаблону(классу)
# '====Аттрибуты и методы==='


# class A:
#     var1 = 'переменная класса'

#     def __init__(self):
#         self.var2 = 'переменная обьекта'

#     def func(self):
#         return 'метод'

# class House:
#     smart_=True
#     class_ = 'comfort+'

#     def __init__(self,color,room_count):
#         self.color=color
#         self.room_count = room_count

#     def action(a):
#         if a=='2 раза хлопнул':
#             print('Свет включен')
#         elif a =='крикнул':
#             print('Звонок в спец.службу')

# h1 = House('green',10)
# h2 = House('red',15)

# _new_ - это метод , который создает пустой обьект(оболочку)
# _init_ -это метод, который после создания засунет туда переменные 
# (этот процесс называется инициализацией)

'=====Принципы ООП======='
# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация(Компазиция, Агрегация)

# Напишите канкулятор на классе с методами add(сумма),percent
# sqrt

class Kalkulytor:

    def Add(self,a,b):
       sum=a+b
       print('Sum:',sum)

    def Percent(self,a,b):
        pros_=(a/100)*b
        print('Persent:',pros_)

    def sqrt(self,a):
        sqrt_= a ** 2
        print('Квадрат числа:',sqrt_)

obg1 = Kalkulytor()
obg1.Add(10,56)
obg1.Percent(81)
obg1.sqrt(5)