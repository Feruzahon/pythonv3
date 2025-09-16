'==============Инкпсуляция=========='
# Инкапсуляция - принцип 

'Напишите CRUD(create, read, update, delete) на миксинах для продуктов, с записью в json'


class CreateMixin:
    def create(self, data):
        ...

class ReadMixin:
    def read(self, data):
        ...

class UpdateMixin:
    def update(self, new_data):
        ...

class DeleteMixin:
    def delete(self):
        ...

class Product(CreateMixin, ReadMixin, ...):
    ...

product1 = {'id':1, 'title':'Nike', 'price':4000}

product = Product()
product.create(product1)