class Wallet: 
  __balance = 0

  def get_balance(self):
    return self.__balance
  
  def deposit(self, amount): 
    self.__balance += amount

  def withdraw(self, amount):
    if (amount > self.__balance):
      print('Недостаточно средств или неверная сумма')
    
    if (self.__balance <= 0):
      print('Недостаточно средств или неверная сумма')

    self.__balance -= amount

    return amount
  
w = Wallet()
w.deposit(500)
w.withdraw(150)

print(w.get_balance())

w = Wallet()
w.deposit(300)
w.withdraw(400)