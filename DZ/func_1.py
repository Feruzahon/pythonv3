'======== 1 ======'
def privet():
    print('Привет Мир!')

privet()

'======= 2 ======'
def name (x):
    print(f'Hello,{x}!')

name(input('What is you name? '))

'======= 3 ======'
def sum(x,y):
    resultat = x+y
    print(f'сумма чисел {x,y}-',resultat)

res = sum(2,4)
res = sum(8,7)

'====== 4 ======'
def proizved(x,y):
    res_tat = x*y
    print(f'Произведение чисел {x,y} = ',res_tat)

proizved(4,5)
proizved(1000,34)

'====== 5 ======'
def name(x):
    print(f'{x}: Гость')

name(input('Ваша имя: '))

'====== 6 ======'
def name_arg(x,y):
    print(f'Имя:{x} Возраст:{y}')

name_arg('Feruza',28)
name_arg(str(input('Name: ')),int(input('age: '))) #универсальное

'====== 7 ======'
def stepen(x):
    res1 = x**2
    res2 = x**3
    print(f'Квадрат: {res1}, Куб: {res2}')

stepen(2)
stepen(int(input('Возведение в степень :  ')))

'====== 8 ======'
def oblast():
    def vlogen():
        return 'Вложенный!'
        
    print('Результат:',vlogen())

oblast()

'========= DOP_1 ======='

def sum_chislo(*args):
    res=0
    for i in args:
        res +=i
    print(res)

sum_chislo(1,3,4,2,6,7,8,9,0)

'========= DOp_2 ======='

def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1)*n#рекурсия 

print(factorial(3))

'========= DOP_3 ======='
kortej = [(1,2),(3,1),(5,0),(2,9)]
lamda_func = sorted(kortej,key = lambda x :x[1])
print(kortej)
print(lamda_func)
