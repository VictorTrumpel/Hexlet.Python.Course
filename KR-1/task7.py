class Worker:
  def __init__(self, name, id, password):
    self.name = name   
    self._id = id             
    self.__password = password  

  def get_id(self):
    print(f"ID (защищенный) → {self._id}")
    return self._id

  def hint(self):
    print(f"Длина пароля (приватный) → {len(self.__password)}")
    return len(self.__password)


class Boss(Worker):
  def __init__(self, name, id, password, count):
    super().__init__(name, id, password)
    self.count = count

  def info(self):
    print(f"Строка: '{self.name} (ID: {self._id})'")
    return f"{self.name} (ID: {self._id})"

e = Worker('Иван Петров', 101, 'alpha')
m = Boss('Анна Сидорова', 205, 'secureKEY', 5)

m.name = 'Анна Сидорова, Глава'
print(f"Чтение публичного имени → '{m.name}'")
m.hint()

m.get_id()
m._id = 206
print(f"ID изменен напрямую (защищенный):→ {m._id}")

m.info()
