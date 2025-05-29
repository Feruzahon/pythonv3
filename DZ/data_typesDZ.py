print('===================Первое задание - арифметические действии ======================')
num1 = int (input('Введите первое число: '))
num2 = int (input('Введите второе число: '))
print('Сумма двух чисел')
print (num1 + num2) #slogenie34
num3 = num1 + num2
print ('Полученное число умножим на *7:')
print(num3 * 7)
num4 = num3*7
print('Число возведем в квадрат получим:' )
print(pow(num4,2))
num5 = pow(num4,2)
print('''Отнимем от квадрата 5555:  
Получем результат:  ''')
print(num5 - 5555)

print('''
''')


print('=========Второе задание связанные - день рождением====')
got_rojdeniy=int(input('Год вашего  рождении: '))
got_progivaniy =int(input('Год вашего проживания:'))
vozrast = got_progivaniy - got_rojdeniy
print('Через 2 года вам будет: ')
print(2+(got_progivaniy-got_rojdeniy))
print('Два года назад вам было:')
print((got_progivaniy-got_rojdeniy)-2)
print('Если умножим ваш возраст на 356 то получим:')
print(vozrast*356)
print('''
''')

print('==============Задание третье==============')
vozrast2 = int(input('Напишите ваш возраст:'))
print('Ваш возраст в единицах СИ:  ')
print(vozrast2*365*24*60*60)
#print('Количество прожитых секундов: ')
#print()

print('''
''')

print('==============Задание четвертое==============')
choklit = int (input('Сколько стоит один шоколад?    '))
milk = int(input('Сколько стоит один литр молока?    '))
coffee = int(input('Сколько стоит одна упаковка кофе?    '))
print('      ')
choklit_kolichestvo = int(input('Количество шоколада:   '))
milk_kolichestvo = int(input('Количество литр молока:   '))
coffee_kolichestvo =int(input('Количество упаковки кофе:    '))
print('Общая стоимость товара:   ')
print((choklit_kolichestvo*choklit) +(milk_kolichestvo* milk )+ (coffee*coffee_kolichestvo))
print('''
''')

print('==============Задание пятое==============')
shirina = int (input('Напишите ширину прямоугольник:  '))
dlina = int (input('Напишите длину прямоугольника:   '))
#периметр прямоугольника:P=2*(a+b)  Площадь прямоугольника:S=a*b
print('Периметр прямоугольника: P=2*(a+b) = ')
print(2*(shirina+dlina))
print('Площадь прямоугольника: S=a*b =  ')
print ( shirina*dlina )
print('')
print('============================================')

