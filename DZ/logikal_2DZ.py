'================Кто старше==========='
name2 = 'Аня'
age1 = int(input('Возраст Ани?'))

name2 ='Сергей'
age2=int(input('Возраст Сергея?'))
#Тернарный оператор
res ='Аня старше Сергея' if age1>age2  else 'Сергей старше Ани'
print(res)

#Классический метод
if age1>age2:
    print('Аня старше Сергея')
elif age1<age2:
    print('Сергей старше Ани')
else:
    print('Аня и Сергей одного возраста')

'============ 2 ================'

email= input('Введите свой email почту:    ')
if email.index('@'):
      print('Почта пользователя- ', email)
# тут я никак не смогла логику придумывать
'================= 3 ==========='
name = input('Введите свое имя:   ')
if name.isalpha():
   if name.istitle():
      print(f'"Привет-{name}!"')
   else:
      print('Неверный формат имени')
else:
   print('Неверный формат имени хотя содержит буквы')


'============== 4 ============='#Завершено
chislo_1 = int(input('Введите число: '))
if chislo_1%2 ==0:
    print(f'Число {chislo_1} - четное')
else:
    print(f'Число {chislo_1} - нечетное')

'============= 5 =========' # можно проверить использу чисел 12,48
chislo_2 =int (input('Введиде число для проверки:  '))
num = chislo_2 ** 2
if chislo_2%2 == 0:
    print(f'Число {chislo_2} - четное')
    if chislo_2%3 ==0:
        print(f'Число {chislo_2} - делится на 3 ')
        if num>1000:
            print(f'Число возведенное в квадрат = {num}')
        else:
            print(f'Число не больше 1000, а равно-{num}')
    else:
        print('Число не делится на 3')
else:
    print(f'Число {chislo_2}- не четное')

'===============  6 ============='#работает

a=int (input('Введите первое число:  '))
b = int (input('Введите второе число:  '))

if a>0 and b>0:
   print(a, 'и' , b,'-Числы положительные')


'============= 7 ============'#

vozrast = int(input('Напишите ваш возраст:  '))
if vozrast >= 18 and vozrast <=119:
    print(f'Вы совершеннолетний {vozrast}')
elif vozrast <=4 and vozrast>=0:
    print('Вы ребенок ', vozrast)
elif vozrast<0 or vozrast>120:
    print('Недопустимый возраст',vozrast)
else:
    print('Несовершеннолеьний',vozrast)