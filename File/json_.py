'=========== JSON ========='
# JavaScript Objekt Notation - универсальный формат данных, понятных почти для всех языков программирования

import json
# json_list = "[1,2,3,4,5]" # массив данные
# json_list = "null" 

# print(type(json_list))

# python_list = json.loads(json_list)
# print(python_list)# list

# # десериализация - перевод json строки в python обьект
# # loads - метод для десериализации с json строки
# # load - метод для десериализации с json файла


# with open('db.json') as file:
#     list_=json.load(file)
#     print(list_)

# сериализация это - перевод python обьекта в json строку

#  dumps -метод для стериализации в json строку 
#  dump - метод для стериализации в json файл

python_list = [1,3,4,5,True,False,None]
json_arrey = json.dumps(python_list)

# from_list = ['Feruza',78,77]
# json_arr = json.dumps(from_list)
# print(json_arr)


with open('db.json','w') as file:
    json.dump(python_list,file)

# with open('db.json','w') as file:
#     json.dump(from_list,file)




