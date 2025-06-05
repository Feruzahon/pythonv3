'==========Модули и пакеты=============='
# любой файл с расширением .py - модуль 
# пакет- это набор модулей (обязательно должен быть такой файл _init_.py)

'==========Работа с файлами==========='
# open - функция , которая открывает файл в определенном режиме

'режим:'
# r-read (тлько для чтения)
# w-write(только для записи, каждый раз файл очищается)
# a- append(только для дозаписи, добавляет в конец)
# x - создает файл, но если он существует выйдет ошибка

'========== Read ======='
# file = open('test.txt','r')
# print(file.writable())# False (проверяет можно ли записывать в этот файл что либо)
# print(file.readable())# True
# print(file.read())#
# file.seek(0)
# print(file.read())#
# # выводит определенную линию
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())



# print(file.readlines())#тут выводить все линии из текста
# file.seek(0)#переташить курсор в начало текста
# print(file.readlines())
# file.closed#False
# file.close()# Файил закрыли
# file.closed#True

'========== Write======='
# file = open('new_file.txt','w')
# # если файил не сушетсвует то файил создас сам с таким названием
# print(file.readable())#False не можем прочитать файл в режиме w
# print(file.writable())#true 

# # file.write('Hello\nworld\n')
# # file.seek(0)
# # file.write('metalabs')

# file.writelines(('AAAA\n','BBBB\n','CCCc\n'))
# file.close()

'======= Append ====='
# file = open('new_file.txt','a')
# file.write('DDDD\n')
# file.close()

'=======Контексный менежер========'
# конструкция with

# with open('test.txt') as f:
#     print(f.closed)#False
#     print(f.read())
#     print(f.closed)#False
# print(f.closed)#True


list2=[-12,4,0,-3,12]
filtered = filter(lambda x:x<0,list2)
print(list(filtered))
