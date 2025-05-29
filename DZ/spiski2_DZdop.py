'================= 8 =========== '  #работает
values = [10,25,8,13,4,7]
list1 =[]
list2 = []

for i in values:
 if i>20:
    print()
 else:
    if i %2 ==0:
        list1.append(i)
    else:
        list2.append(i)
print(f'четные число - {list1}')
print(f'нечетные число - {list2}')

'================= 9 ============='
spisok = ['Feruza','Mamaraimova','Ali','Mama','lev']
spisok.sort(key=len)
print(spisok)

for i in spisok:
   a = len(i)
   if a >= 8:
      print(f'Слишком длинное слово - {a}, -{i}')
   else:
      print(f' Cлова в порядке - {a} , - {i}')
'========================= 10 ===================='

spisok = input('напишите строку:  ')
slova = spisok.split()# по словам
element = list(reversed(spisok))#по элементам

print('список слов: - ',slova)
print('список символов в слове: - ',element)
for i in element:
    if i.isdigit():
        i = int(i)
        print(f'Найдено число - {i}')
    else:
     print('цифр нет')

    # в этом части не могла придумать цикл про остановки, забыла работы while так как видео не досмотрела