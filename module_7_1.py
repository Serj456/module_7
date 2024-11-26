from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return "{}, {}, {}".format(self.name, self.weight, self.category)

class Shop:
    __filename = "products2.txt"
    def get_products(self):
        with open('products2.txt','r+', encoding='utf-8') as file:
            rs = file.read()
            return rs
            file.close()


    def add(self, *products):
        for i in products:
            search_term = str(i)
            with open('products2.txt','r+', encoding='utf-8') as file:
                content = file.read()
                if search_term in content:
                    print(f'Продукт {i.name} уже есть в магазине')
                    pass
                else:
                    file.writelines(search_term + "\n")

        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
