"------ Полиморфизимз-----"
# Полиморфизим - принцип ООп, в котором в разных классах 
# метод называется одинакова, но с разным реализациями

class Dog:
    def voice(self):
        print('гав-гав')

class Cat:
    def voice(self):
        print('мяу-мяу')

class Frog:
    def voice(self):
        print('ква-ква')

objects=[Dog(),Cat(),Frog()]
for obj in objects:
    obj.voice()

10 + 4 # 14
'hello'+'world'  #helloworld
