'========== Наследование ======='
# наследование - принцип ООп, в котором мы можем унаследовать, переопределить и использовать 
# в дочерном классе все атребуты и методы родительского класса

# class A:
#     def say_hello(self):

#         print('Привет! Я из родительского ')
#     def age(self):
#         print('19')

# class B(A):
#     ...

# obj_a =A()
# obj_a.say_hello()
# print(obj_a.age)

# obj_b=B()
# obj_b.say_hello()
# print(obj_b.age)


# class Viecal():
#     def repair():
#         print(' я ченю машину')
# "Пример одиночное наследование"
# class Animals():
#     def voice(self):
#         print('Я животное, издаю звук.')
# # переопределение
# class Cat(Animals,Viecal):#  нету смысла наследовать ненужный класс
#     def voice(self):
#         print('Миу')

# dog1 = Animals()
# dog1.voice()


# cat1 = Cat()
# cat1.voice()


# """"
# Виды наследование
# 1) Одиночное наследование- когда дочерный класс наследуется только от одного класса
# 2) Множественное наследование - когда дочерный класс может инаследовать от нескольких классов сразу
# 3) Многоуровневые наследование - когда мы наследуемся от класса у которого есть родитель
# 4) Иерархическая наследование - когда у одного родительного есть много дочерных классов
# 5) Гибридное наследование - когда мы можем использовать сразу нескольво видов наследование
# """

# class A:
#     ...
# class B:
#     ...

# class C:
#     ...
# class D:
#     ...

# class E(A,B,C,D):# Мнодественное
#     ...

# "Многоуровневое наследование"
# class A:
#     ...
# class B(A):
#     ...
# class C(B):
#     ...
# class D(C):
#     ...

# "Иерархическая"

# class A:
#     ...
# class B(A):# 
#     ...
# class C(A):
#     ...
# class D(A):
#     ...

# 'Гибридное'

# class A:
#     ...
# class B(A):# Иерархическое так как Б и С наследунт от А
#     ...
# class C(A):
#     ...
# class D(C,B):# Множественное так как наследуется от двух классов
#     ...

"""
Класс object - самый главный в иерархии класс, от него наследуется любой класс, который вы создадите
"""

class Car():
    ...

car = Car()
print(dir(car))

"""

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
"""
# dir -возврашает все методы которые используется 
#  Хоть и внутри класса car мы ничего не использовали , любой класс всегда наследует от oblect - и принимает все его методы и атрибуты и паказано ввыше

