class publisher:
    def __init__(self,name):
        self.name=name
        
    
class book(publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.author=author
        self.title=title
class python(book):
    def __init__(self, name, title, author,price,pages):
        super().__init__(name, title, author)
        self.price=price
        self.pages=pages
    def display(self):
        print(f"Publisher:{self.name}")
        print(f"Name:{self.title}")
        print(f"Price:{self.price}")
        print(f"Author:{self.author}")
        print(f"Price:{self.price}")
        print(f"Number of pages:{self.pages}")
        
obj= python("Pearson Education","Core python Applications","Wesley J.",500,1200)
obj.display()

