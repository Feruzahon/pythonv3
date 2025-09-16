'------методы----'
# classmethod (cls) - указывает , что метод классметод, cls ссылка на сам класс

class Myclass:
    var = 3
    @classmethod
    def my_method(cls,var1):
        cls.var += var1

Myclass.my_method(2)
print(Myclass.var)



class Student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

    @classmethod
    def get_count(cls):
        print('Количество студентов равно:')
        return cls.count
    
s1 = Student('Feruza',21)
s2 = Student('Alisa',3)
s3 = Student('Alisa',34)

print(Student.get_count())
'Алтернативный метод'
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls,string):
        name, age = string.split(',')
        return cls(name, int(age))
    
p = Person.from_string('Feruza,28')
print(p.name , p.age)


'----статистический метод---'

class Test:
    @staticmethod
    def static_hello():
        print('hello(no self or cls)')
    @classmethod
    def class_hello(cls):
        print(f'hello from {cls.__name__}')

    def instance_hello(self):
        print(f'hello from {self}')

Test.static_hello()
Test.class_hello()

t = Test()
t.instance_hello()


' ------ Практика ----'
class Dog:
    total_dogs = 0

    def __init__(self,name):
        self.name = name
        print(f'Имя собаки {self.name}')
        Dog.total_dogs +=1

    @classmethod
    def get_total(cls):
        print(f'Колтчество собак: ')
        return cls.total_dogs
    
dog1 = Dog('Reks')
dog2 =Dog('Hatiko')
dog3 = Dog('Riza')

print(Dog.get_total())
'-2'
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    @classmethod  
    def from_string(cls,string):
        title,author = string.split(';')
        return cls(title, author)
    
b = Book.from_string('Война и мир ; Толстой')
print(b.title , b.author)
