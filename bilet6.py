class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        pass
    
class Novel(Book):
    def __init__(self, title, author, year):
        super().__init__(title, author, year)
        
    def get_info(self):
        print(f"Книга {self. title} автора {self.author} написана в жанре ноовелла. Новелла (от итал. novella — новость) — малый эпический жанр, написанный в прозе. ")
    
class Poetry(Book):
    def __init__(self, title, author, year):
        super().__init__(title, author, year)
        
    def get_info(self):
        print(f"Книга {self.title} автора {self.author} написана в жанре поэзия. Поэзия (греч. poiesis, от poieo — творю, создаю) — наряду с прозой один из двух основных способов организации художественной речи.")
        

b1 = Novel('Последний лист' , 'О. Генри', 1907)
b2 = Poetry('Парус', 'М.Ю. Лермонтов', 1832)

b1.get_info()
b2.get_info()

