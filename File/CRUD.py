import json

# CRUD - Create, Read, Update, Delet

def creat_product(new_product, file):#  добавить
    with open(file,'r+') as f:
        products=json.load(f)
        products.append(new_product)
        json.dump(products,f)
    print('Вы успешно добавили товар!')

creat_product()

def read_products (file): # смотреть продукт
    ...

def read_product(id,file): # добавить по отдельности
    ...

def update_product(id,file): # 
    ...

def delet_product(id,file):# удалить
    ...

# 