from sqlalchemy import create_engine, Column, Integer,String
from sqlalchemy.orm import declarative_base, sessionmaker

# ссылка к базе данных
db_url= 'postgresql://feruza:1@127.0.0.1:5432/orm_db'

#подключение к бд
engine = create_engine(db_url)


#базовый класс для создания таблиц
Base = declarative_base()

#создание таблиц
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key =True)
    title = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f'{self.id} -> {self.title} -> {self.price}'
    # тут сделали код читабельно

#записываем таблицу в бд
Base.metadata.create_all(bind=engine)

#создаем класс для сессий
SessionLocal = sessionmaker(bind = engine)

#создаем ссесию (связываем)
session = SessionLocal()
'--------CREATE------------'
#создали продукт Nike при помощи класс Product (заполняем таблицы в бд вручную)
# product1 = Product(title = 'Nike', price = 400)

#добавляем продукт в сессию
# session.add(product1)

# #отправляем запрос в бд
# session.commit()

'--------Read------------'
#стяягиваем все записи с таблицы  Product 
# products = session.query(Product).all()

# # product001 = session.get(Product,3)

# print(products)

'------Update----------------'
# product2 = session.get(Product,2)
# print(product2)

# product2.title = 'Nokey'
# session.commit()

# product2.price = 1200
# session.commit()

# product2 = session.get(Product,2)
# print(product2)

# '-----Delete ------'
product3= session.get(Product,3)
print(product3)

session.delete(product3)
session.commit()

product3= session.get(Product,3)
print(product3)


