import json

# CRUD - Create, Read, Update, Delet

def creat_product(new_product, file):#  добавить
    with open(file) as f:
        products=json.load(f)
        products.append(new_product)# [{"title":"iphone 13Pro"}]
    with open(file, 'w') as f:
        json.dump(products,f, indent = 2)
    print('Вы успешно добавили товар!')

creat_product({"id":3 ,"title":"adidas", "price":250},"shop_db.json")
creat_product({"id":4,"title":"toyota", "price":7000},"shop_db.json")


def read_products (file): # смотреть продукт
    with open(file) as f:
        products = json.load(f)
        for product in products:
            print(f"Товар:{product['title']}, стоит {product['price']}$")

# read_products("shop_db.json")

def read_product(id,file): # добавить по отдельности читает определенный продукт
    with open(file) as f:
        products = json.load(f)
        for product in products:
            if product["id"]==id:
                print(f"Товар: {product['title']},стоимость {product['price']}$")
                break
        else:
            print('По такому id продукт не существует!')

        
id_tovara = int(input('Выведите Id товара для полной информации '))
read_product(id_tovara,"shop_db.json")

# сработала изменение цена продукта
def update_product(id,file): # меняет наш продукт например цену
    with open(file) as f:
        products = json.load(f)
        for product in products:
            if product["id"]==id:
                product["price"]=400
                print('Цена изменена успешно')
    with open(file,'w') as f:
        json.dump(products,f,indent=2)

# update_product(4,"shop_db.json")

# завершила удаление только продукт 
def delet_product(id,file):# удалить продкт
    with open(file) as f:
        products = json.load(f)
        for i, product in enumerate(products):
            if product["id"]==id:
                del products[i]
                print('Продукт удален!')
                break
        else:
            print('Продукт не найден!')

    with open(file,'w') as f:
        json.dump(products,f,indent=2)

delet_product(4,"shop_db.json")
