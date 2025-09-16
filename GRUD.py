import json

class CreateMixin:
    def create(self, data):
        with open('products.json', 'r') as f:
            products = json.load(f)
        products.append(data)
        with open('products.json', 'w') as f:
            json.dump(products, f, indent=4)

class ReadMixin:
    def read(self):
        with open('products.json', 'r') as f:
            return json.load(f)

class UpdateMixin:
    def update(self, index, new_data):
        with open('products.json', 'r') as f:
            products = json.load(f)
        products[index] = new_data
        with open('products.json', 'w') as f:
            json.dump(products, f, indent=4)

class DeleteMixin:
    def delete(self, index):
        with open('products.json', 'r') as f:
            products = json.load(f)
        products.pop(index)
        with open('products.json', 'w') as f:
            json.dump(products, f, indent=4)

class Product(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    pass

product = Product()

product.create({'id': 1, 'title': 'Nike', 'price': 4000})
product.create({'id': 2, 'title': 'Adidas', 'price': 3500})

print('Все продукты:', product.read())

product.update(0, {'id': 1, 'title': 'Nike Air', 'price': 4500})

print('После обновления:', product.read())

product.delete(1)

print('После удаления:', product.read())