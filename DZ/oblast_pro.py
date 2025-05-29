'======== 1. ======='
name = 'Feruza'
age = 28

def func1():
    global name, age
    print(name,age)

func1()

'======== 2. ======='
def func2():
    name = 'Ali'
    age =3
    print(f'Name {name}, Age - {age}')

func2()
'======== 3. ======='
def func3():
    x=25
    print(x)

#print(x) # ошибка так как глобальное пространство не видет переменную внутри локальной
# print(x) 
#       ^
# NameError: name 'x' is not defined


'======== 4. ======='
count = 'Hello' 

def func4():
    global count
    print(count)
    count = 'Привет!'
    print('Измениналась на  -' ,count)

func4()

'======== 5. ======='
def func7():
    name ='Ali'
    def func8():
        print('Внешняя переменная',name)
    func8()

func7()

'======== 6. ======='
def func5():
    count = 77
    def func6():
        nonlocal count
        print(count)
        count = 'изменено'
        print('обновленное значение:',count)
    
    func6()
func5()

'======== 7. ======='
# 1 -способ
count = 1
def func9():
    global count
    print('Снаружи функции', count)
    count = 'Feruza'
    print('Внутри функции:',count) 
func9()

# 2 -способ
count = 1
def func9():
    count = 'Feruza'
    print('Внутри функции:',count) 

func9()
print('Снаружи функции', count)

'======== 8. ======='
count = [1,2,3,4,5,6]
for i in count:
    name = 'Feruza'
    print('Число - ',i)

print('Переменная доступна',name) # доступна так как эти переменные находится в глобальном пространстве 

'======== 9. ======='
# name = 'Ali'
# # def func11(name):
# #     # global name # невазможна ссылаться на глобальную переменную так как такое переменное уже есть в функции
# #     print(name)

# # func11('Feruza')
# # print(name)

x=10
def func12(x):
    print('Внутри функции',x)

func12(5)
print('Снаружи функции',x)
