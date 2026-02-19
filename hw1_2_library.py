libr1=[]
def add_book(library:list, title:str, author:str, year:int, genre:str):
    d = {
    'title':title,
    'author':author,
    'year':year,
    'genre':genre,
    }
    library.append(d)
    return print('Книга добавлена в библиотеку')

def remove_book(library:list, title:str):
    for book in library:    
        library.remove(book) if book.get('title')==title else 0
    return print('Книга убрана из библиотеки')

def find_books_by_author(library:list, author:str):
    for book in library:
        print('найдена книга', book.get('title'), ': (', book.get('author'), book.get('year'),')') if book.get('author')==author else 0
    return print('поиск завершен')

def find_books_by_genre(library=list, genre=str):
    for book in library:
        print('найдена книга', book.get('title'), ': (', book.get('author'), book.get('year'),')') if book.get('genre')==genre else 0
    return print('поиск завершен')

def get_books_published_after(library:list, year:int):
    for book in library:
        print('найдена книга', book.get('title'), ': (', book.get('author'), book.get('year'),')') if book.get('year')>year else 0
    return print('поиск завершен')

def get_library_statistics(library:list):
    genres=sorted([[[i.get('genre') for i in library].count(_), _] for _ in set(([o.get('genre') for o in library]))],reverse=True)
    d={
    'book_count':len(library),
    'author_count':len(set([i.get('author') for i in library])),
    'most_pop_genre':[i[-1] for i in genres if i[0]==max([i[0] for i in genres])],
    'earliest':min([i.get('year') for i in library])
    }
    return d