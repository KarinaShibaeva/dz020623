class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_info(self):
        pass
    
class Food(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        
    def get_info(self):
        print(f"Товар {self.name} стоит {self.price} и относится к категории еда.")
    
class Electronics(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        
    def get_info(self):
        print(f"Товар {self.name} стоит {self.price} и относится к категории электроника.")
        
p1 = Food('Яблоко', '90р')
p2 = Electronics('Телевизор', '35 000р')

p1.get_info()
p2.get_info()