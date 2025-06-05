import json

'========== 1 ========'
# with open('data.json','r') as file:
#     list_1 = json.load(file)
#     print(list_1)

'======== 2 =========='
# dict_1 ={
#     'name':'Feruza',
#     'age':28,
#     'email':'mamraimova@mail.ru'
# }

# with open("user.json",'w') as file:
#     json.dump(dict_1,file, indent=2)
# print('Вы успешно записали данные на файл!')

'========= 3 ======='
# json_list='{"product": "Laptop", "price": 1200, "in_stock": true}'
# python_list = json.loads(json_list)

# print('Десериализованная строка:\n',python_list)
# print('Значения ключа price:\n',python_list['price'])
'========== 4 ======='
def read_product(id,file):
    with open(file) as f:
        product = json.load(f)
        for i in product:
            if i['id']==id:
                print(f"Товар: {i['name']}, стоит {i['price']}$")
                break
        else:
            print('Товар по такому id не найден!!!')

# read_product(2,"products.json")# выводит  данные
# read_product(5,"products.json")# показывает сообщение что нет

'========== 5 ======='
def update_key(key,file):
    with open(file) as f:
        config_key =json.load(f) 
        print(config_key)
        if config_key['theme']==key:
            config_key['theme']='dark'
            print('Успешно обновлена ключ!')
        else:
            print('Такого ключа нету, не можем провести обновление!!!')
    with open(file,'w') as f:
        json.dump(config_key,f,indent=2)
        print(config_key)

# update_key('light',"config.json")

'========= 6 ======='

def filter_student():
    with open('students.json') as file:
        dict_students = json.load(file)
    
    top_students=[]

    for students in dict_students:
        if students['score']>=80:
            print(f"Имя студента {students['name']}, Набранный бал: {students['score']}")
            top_students.append(students)
    
    with open('top_students.json','w') as file:
        json.dump(top_students,file,indent=2)

    print('Студенты добавлены успешно на новый файл!')
 

# filter_student()

'======== 7 ======'
with open('employees1.json') as file:
    list_1 = json.load(file)

with open('employees2.json') as file:
    list_2 = json.load(file)

result= list_1+list_2

set_1={}
for i in result:
    set_1[i['id']]=i

list_3 = list(set_1.values())
print(list_3)

with open("all_employees.json",'a')as file:# тут использовала 'a' чтобы сохранить и создать json файл автоматически
    json.dump(list_3,file, indent=2)

print('Данные добавлены успешно!')