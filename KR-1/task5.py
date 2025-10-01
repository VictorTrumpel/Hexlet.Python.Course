class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __str__(self):
    return self.title


class Reader:
  def __init__(self, fio, card_number, faculty, birth_date, phone):
    self.fio = fio
    self.card_number = card_number
    self.faculty = faculty
    self.birth_date = birth_date
    self.phone = phone

  def takeBook(self, *args):
    if len(args) == 1 and isinstance(args[0], int):  
      print(f"{self.fio} взял {args[0]} книги(и).")
    else:
      titles = [arg.title if isinstance(arg, Book) else str(arg) for arg in args]
      print(f"{self.fio} взял книги: {', '.join(titles)}.")

  def returnBook(self, *args):
    if len(args) == 1 and isinstance(args[0], int):  
      print(f"{self.fio} вернул {args[0]} книги(и).")
    else:
      titles = [arg.title if isinstance(arg, Book) else str(arg) for arg in args]
      print(f"{self.fio} вернул книги: {', '.join(titles)}.")

reader = Reader('Петров В. В.', 1001, 'ФИТ', '01.01.2000', '8900...')

book1 = Book('Война и мир', 'Л.Н. Толстой')
book2 = Book('Атлант расправил плечи', 'Айн Рэнд')

reader.takeBook(4)
reader.takeBook('География', 'Физика')
reader.takeBook(book1, book2)

reader.returnBook(3)
reader.returnBook('Мастер и Маргарита book1')