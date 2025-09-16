'---------------Ассоциация---------'
# Ассщциация - это принцип ООп, в котором 2 класса 
# связанные друг с другом


# Агрегация-слабая связь
# Компрозиция - сильная связь

'композиция'
class Battery():
    _power = 100
    def charge(self):
        if self._power <100:
            self._power = 1000


class Iphone:
    def __init__(self,color):
        self.color = color
        self.battery = Battery()

iphon = Iphone('Красный')
del iphon
# удалилась 


'Агрегация'
class Nokia:
    def __init__(self,color, battery):
        self.color = color
        self.battery = battery

battery_for_nokia = Battery()
nokia = Nokia('green',battery_for_nokia)

del nokia