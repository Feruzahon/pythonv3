'----------------Абстракция---------------'
# Абстракция - это принцип ООп в котором, создается класс 
# пустышка где задаются названия для методов и атрибутов для 
# того чтобы не забыть переопределить их в дочерном классе

from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def voice(self):
        ...

    @property
    @abstractmethod
    def legs(self):
        ...

class Dog(AbstractAnimal):
    legs = 4
    def voice(self):
        print('гав-гав')

obj = Dog()
obj.voice()

class Cat(AbstractAnimal):
    legs = 4
    def voice(self):
        print('мяу-мяу')


    def hunt(self):
        print("охочу")

obj =Cat()
obj.voice()
obj.hunt()

