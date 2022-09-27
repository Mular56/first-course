import pandas as pd

class Library:
    data=pd.DataFrame()
    
    def add_book(self, name:str, author: str, year: int, genre: str):
        data_dictionary={"Название":name, "Автор": author, "Год": year, "Жанр": genre}
        self.data=self.data.append(data_dictionary, ignore_index=True)
        print(self.data)
    def delete_book(self, book_id: int):
        if len(self.data) == 0:
            print("Нет книг в библиотеке")
        else:
            self.data=self.data.drop(book_id)
            print(self.data)

    def find_book(self, book_id: int):
        all_indexes = self.data.head()
        for i in all_indexes.index:
            if all_indexes.index[i] == book_id:
                print(pd.DataFrame(self.data.iloc[book_id]))     
l=Library()
l.add_book("Незнакомка","Александр Блок", 1906,"Худ.вымысел")
l.add_book("Я вас любил","Александр Пушкин",1829 ,"Стихотворение")

or1 = int(input('Вы хотите добавить книгу в библиотеку? (1 - Да, 2 - Нет)\n '))
if or1 == 1:
    rang1 = int(input('Введите количество книг, которые вы хотите добавить в библиотеку\n '))
    for i in range(rang1):
        name = input("Название:")
        author = input("Автор:")   
        year = input("Год:")
        genre = input("Жанр:")
        l.add_book(name, author, year, genre)
else:
    exit
    
del1 = int(input("Желаете ли вы удалить книгу из библиотеки? (1 - Да, 2 - Нет)\n"))
if del1 == 1:
    ch = int(input("Какой номер книги вы хотите удалить?\n"))
    l.delete_book(ch)
else:
    exit

find = int(input("Желаете ли вы найти книги по номеру?(1 - Да, 2 - Нет)\n"))
if find == 1:
    ch2 = int(input("Введите номер книги\n"))
    l.find_book(ch2)
else: 
    exit
