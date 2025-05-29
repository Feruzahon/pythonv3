'===========   1  =============='#работала
list1 = [7,28,3,'Feruza',3, 'Ali',True,[5,7,0,[2,7,3]]]
print(list1[-1][-1][1],'-второй элемент из выложенного списка')

'======= 2 ========='#сработала
list = [14,7,'Feruza','Ali','Islam',23,28,3,4]
print(list)
peremeniy = list.pop(0)
print(peremeniy,'-удаленный элемен')
print(list,'список после удаленного элемента')

'=========== 3 ========='#сработала
list1 = ['hello',42,True,'word',False,42]
list1.remove('hello')#remove -удаляет элемент в списке по значению
print(list1)

'========== 4 ==========' #закончила
list2 = ['simpel','hard','advenced','bacic']
print(list2,'-изначальный список')
list2.insert(2,'medium')
print(list2,'-изменённый список')

'============ 5 ========'#закончила
first = [1,2]
second = [3,4]
first.extend(second)
#first [2:2] = second #быстрый способ
#new_list = first + second # то что касается сложением строк
print(first)
# print(new_list)

'============== 6 =============='
mixed = ['cat','3','python','1.5','a','elephont']#строка
# #1   случии когда все значение строки
mixed.sort(key=len)
print(mixed,'-сортировка по возрастанию строк')

# #2 когда использую сортировку
list3 = ['cat',3,'python',1.5,'a','elephont']
stroka = [x for x in list3 if isinstance(x,str)]#фильтир от чисел ##нашла с интернета
stroka.sort(key=len)
print(stroka,'-сортировка по количество букв в слове')

'========= 7 ==========='
kartej = (7,3,'Feruza','Ali',[28,3,3,[-3,3]])
print(kartej[3],'-вывод по индекцу')#
print(kartej.count(3),'-вывод по заданному значению')#

kartej.insert(2,'hi')
print(kartej)
#не работает другие  методы так как tupl(кортеж)-неизменяемый тип дланных