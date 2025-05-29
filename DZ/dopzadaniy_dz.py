#'==== 1 ====='
print('=======  1  =======')
name = input('Ведите вашу имию :  ')
age = int(input('Ведите ваш возраст:  '))

info = f'Студент из группы МК(м) 1-14: {name}\n Возраст: {age} '
print (info)

info1 = 'Студент из группы МК(м) 1-24: {} \n Возраст: {} '
print (info1.format('Myhammadali',25 ))

print('  ')


#'========= 2 =========='

print('======== 2 ========')
predlojeniy = input ('Несколько строк из любимых песень:   ')
print(predlojeniy.replace(' ','-' ))
print('  ')

#'======== 3 ========='

print('====== 3  ======')
stroka = input ('Автор романа "Война и мир?"  ')
print(stroka.isalpha()) 
print('  ')


#'======== 4 ========'
print('==== 4 ======')
stroka1 = input('Ваша имя на английском языке:  ')
print(stroka1.lower(), '-lower')
print(stroka1.upper(), '-upper')
print(stroka1.swapcase(), '-swapcase')
print(stroka1.count('a'), "  - count 'a'")
print(stroka1.startswith('f'), " - startswit 'f' ")
print(stroka1.endswith('a'), "- endswith 'a' ")
print(stroka1.islower())
print('  ')


#'======== 5 ========'
print('====== 5  ======')
stroka2 = input ('Напишите первый куплет вашей любимой песни:  ')
razrez = input('Выберите букву из вашего слова:  ')
print('1-символ из предложение   ',stroka2[2:3])
print('Последняя буква из предложение:  ',stroka2[-1:])
print(stroka2.split(razrez ), ' - разрез по выбранному букву')
print('предложение в отзеркалном положение:  ', stroka2[::-1])
