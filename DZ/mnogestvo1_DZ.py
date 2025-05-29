'=========== Задание 1. ========'

dict1 ={'name':'Feruza','age': 28,'profeshion':'dev'}
print(dict1.get('profeshion'))
print(dict1['name'])

'=========== Задание 2. =========='
product = {
    'name':'phone',
    'price':1000
}

product['price']=1200
product['brand']='Samsung'
print(product)

'============ Задание 3. ========='
dict1 =dict.fromkeys(['p','y','t','h','o','n'],0)
print(dict1)

'================= задание 4. ==========='
user = {
    'name':'Alice',
    'age':25
}
user_pop = user.pop('age')
print(user_pop)

'================= задание 5 =========='
info = {
    'city':'Paris',
    'population':2148327
}
for kye in info.keys():
   if kye == 'city':
      print('Ключ найден')
else:
     print('Ключ не найдет')


'============ Задача 6. ========='
numberas = [1,2,2,3,4,4,5,1]
set1 = set(numberas)
print(set1)
'============= 7 ============='
set1 = {1, 2, 3}
set2 = {3, 4, 5}

cammon = set1 & set2 # обьединение множеств , пересечение множеств
cammon1= set1.intersection(set2)
print(cammon1)
print(cammon)

'================== 8 ==================='
grades = {
    'John': 85, 
    'Jane': 92,
    'Dave':58
  }

for name,grade in grades.items():
    if grade>80:
        print(f'У студента {name} оценка {grade}')
    elif grade==58:
        print('Нашелся студент у которого 58 баллов')
