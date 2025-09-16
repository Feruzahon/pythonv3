'==============Инкпсуляция=========='
# Инкапсуляция - принцип ООП у которого 2 трактовки

#1. Сбор всех необходимых аттрибутов в одну капсулу (класс)
#2. Сокрытие данных (ограничение доступа к аттрибутам)

'Виды доступа к аттрибутам'
# 1. public (публичные)
# 2. protected (защищенный) - с одним underscore в начале
# 3. private (приватный) - с двумя underscore в начале

# class A:
#     attr1 = 'public'
#     _attr2 = 'protected'
#     __attr3 = 'private'

# print(A.attr1)
# print(A._attr2)
# print(A._A__attr3)

# # obj_a = A()
# print(A.__dict__)


'=============Getters/Setters============='
# функции, с помощью которых можно получить/изменить значение аттрибута 


# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.__age = age

#     def get_age(self):
#         return self.__age
    
#     def set_age(self, new_age):
#         self.__age = new_age


# obj = Person('Katana', 21)
# # obj._Person__age = 27

# print(obj.get_age())
# obj.set_age(30)
# print(obj.get_age())


# class Person:


    
#     def __init__(self, name, age):
#         self.name = name 
#         self.__age = age 

    # @property 
    # def age(self):
    #     return self.__age

    
    # @age.setter
    # def age(self, new_age):
    #     self.__age = new_age

# print(Person('katana', 22).__dict__)
# obj = Person('Anon', 30)
# print(obj.age)
# obj.age = 25
# print(obj.age)

'Напишите CRUD(create, read, update, delete) на миксинах для продуктов, с записью в json'
import json

FILE_NAME = 'products.json'


def read_from_file():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def write_to_file(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)


class CreateMixin:
     def create(self, data: dict):
        products = read_from_file()
        products.append(data)
        write_to_file(products)

class ReadMixin:
     def read(self, product_id=None):
        products = read_from_file()
        if product_id is None:
            return products
        for product in products:
            if product.get('id') == product_id:
                return product
        return None

class UpdateMixin:
   def update(self, product_id, new_data: dict):
        products = read_from_file()
        for i, product in enumerate(products):
            if product.get('id') == product_id:
                products[i].update(new_data)
                write_to_file(products)
                return
        print('Продукт не найден')

class DeleteMixin:
    def delete(self, product_id):
        products = read_from_file()
        new_products = [p for p in products if p.get('id') != product_id]
        write_to_file(new_products)


class Product(CreateMixin, ReadMixin, UpdateMixin,DeleteMixin):
    ...

product1 = {'id':1, 'title':'Nike', 'price':4000}

product = Product()
product.create(product1)

print(product.read())
print(product.read(1))

product.update(1, {'price': 4200, 'title': 'Nike Air'})
product.delete(2)


