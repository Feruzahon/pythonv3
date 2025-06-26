'======= 1 =========работает'
class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f'Привет меня зовут {self.name}')

class Student(Person):
    print('Я студент:')
obj1 = Person('Ali')
obj1.introduce()

obj2 = Student('Feruza')
obj2.introduce()

'==========2 ==========работает'

class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f'Привет меня зовут {self.name}')

class Student(Person):
    def show_grade(self,grade):
        print( f'Полученная оценка: {grade}')


obj2 = Student('Feruza')
obj2.introduce()
obj2.show_grade('5')


'====== 3 ====работает'

class Animal():
    def make_sound(self,zvuc):
        print(f'Это животное издает звук." {zvuc}" ')

class Dog(Animal):
    print('Собока')

object_2 = Dog()
object_2.make_sound('Гав')


'====== 4 ===работает'
"""
Kia K7, также известная как Kia Cadenza, 
оснащается различными двигателями, включая бензиновые, 
дизельные и гибридные. Наиболее распространены бензиновые 
двигатели объемом 2.4, 2.5, 3.0 и 3.3 литра. Дизельный двигатель,
2.2-литровый R e-VGT, доступен в некоторых комплектациях.
Гибридная версия включает 2.4-литровый бензиновый двигатель. 
Колеса Kia K7 обычно имеют размерность 225/55 R17, 
но могут варьироваться в зависимости от комплектации. 

использовала этот текст для работы
"""
# двигатель
class Engine:
    def descripbe_engine(self,ob ):
        print(f'Двигатель объемом: {ob} литра')
# колеса
class Wheels:
    def describe_wheeles(self,razmer):
        print(f'Размер колеса: {razmer}')

class Car(Engine,Wheels):
    def name_car(self,name):
        print(f'Название машин:{name}')

obj3 = Car()
obj3.name_car('Kia K7')
obj3.descripbe_engine('2.4')
obj3.describe_wheeles('225/55 R7')

'===== 5 ====работает'
# наследование для вывода информации ученика 
class A:#имя
    def __init__(self,name):
        self.name = name
        
    def show_A(self):
        print(f'Имя ученика:{self.name}')

class B(A):# группа
    def show_B(self,grup):
        print(f'Обучающая группа : {grup}')
class C(B):#оценки за четверть по математике
    def show_C(self,one,two, three, fore):
        print(f"Оценка за 1- четверть {one} \nОценка за 2- четверть {two}")
        print(f"Оценка за 3- четверть {three} \nОценка за 4- четверть {fore}")
obj4 = C("Feruza")
obj4.show_A()
obj4.show_B("5-B")
obj4.show_C('5','4','5','3')

'======= 6 ======работает'

class Animals:
    def __init__(self,name):
        self.name = name
    def sound_A(self):
        print(f'Я - {self.name}')

class Cat(Animals):
    def sound_Cat(self):
        print('Умею ловить мыш.')

class Dog(Animals):
    def sound_Doq(self):
        print('Умею сторожить дом.')

class Bird(Animals):
    def sound_Bird(self):
        print('Умею летать.')


obj5 = Cat('Кошка')
obj5.sound_A()
obj5.sound_Cat()


obj6 = Dog('Собака')
obj6.sound_A()
obj6.sound_Doq()

obj7 = Bird('Птица')
obj7.sound_A()
obj7.sound_Bird()

'===== 7  ====работает'
class A:
    def __init__(self,name_f,name_m):
        self.fathe = name_f
        self.mathe = name_m
    def class_A(self):
        print(f'Отец:{self.fathe}\nМать: {self.mathe}')

class B(A):#Сын
    def class_B(self,name):
         print(f'Сын: {name}')

class C(A):#Дочь
    def class_C(self,name):
        print(f'Дочь: {name}')

class D(B,C):
    def class_D(self):
        print('У нас есть дети:')

obj8 = B('Ислам', 'Феруза')
obj8.class_A()
obj8.class_B('Мухаммадали')

print('--------------')
obj9 = C('Ислам','Феруза')
obj9.class_A()
obj9.class_C('Жасмин')

print('--------------')
obj10 = D('Ислам','Феруза')
obj10.class_A()
obj10.class_D()
obj10.class_B('Мухаммадали')
obj10.class_C('Жасмин')

'======= 8 =====работает'
class A:
    def __init__(self,name):
        self.name_ticher = name
        print(f'Привет Я учительница - {self.name_ticher}')

class B(A):
    def __init__(self, name):
        super().__init__(name)
        print('Преподаю математику')

class C(A):
    def __init__(self, name):
        super().__init__(name)
        print('Преподаю Биологию')

obj11 = B('Феруза Абдухалимовна')
obj12 = C('Ирода Музафаржановна')

'====== 9 ====работает'
# транспортное средство
class Vehicle:
    def __init__(self,name):
        self.name = name
        print(f'Название:{self.name}')

# Мошина
class Car(Vehicle):
    def car(self):
        print('Передвигается по дороге')
#лодка
class Boat(Vehicle):
    def boat(self):
        print('Передвигается по воде')
#автомобиль-амфибия
class AmphibiousCar(Car,Boat):
    def amphibiy(self):
        print('Транстпортное средcтво вездехон:')

obj13 = Car('Bentley')
obj13.car()
print('----------------')

obj14 = Boat('Дельфин')
obj14.boat()

print('----------------')
obj15 = AmphibiousCar('Ford GPA')
obj15.amphibiy()
obj15.car()
obj15.boat()

'======= 10 =====работает'
class Animal:
    def __init__(self,name):
        self.name = name
    def name_s(self):
        print(f'{self.name}-относится к')

        
#млекопитающее
class Mammal(Animal):
    def mammal(self):
        print('Млекопитающим - это животная которая вскармливают своих детей молоком')
#птица
class Bird(Animal):
    def bird(self):
        print('Птитцам- это живатные которые имеют крылья, клюквыв и оперение.')


# Летуча мышь
class Bat(Mammal):
    def __init__(self, name):
        super().__init__(name)
    def bat(self):
        print('Которая питаются:насекомыми, фруктыми. ')

# Пингвин
class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)
    def pingvin(self):
        print('Которая питаются: рыбами, головоногими малюсками')

obj16 = Bat('Летучий мышь')
obj16.name_s()
obj16.mammal()
obj16.bat()
print('------------')

obj17 = Penguin('Пингвин')
obj17.name_s()
obj17.bird()
obj17.pingvin()