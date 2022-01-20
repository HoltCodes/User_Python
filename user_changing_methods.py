class User:

  def __init__(self, name):
    self.name = name
    self.amount = 0

  def make_deposit(self, amount):
    self.amount += amount
    

  def make_withdrawlal(self, amount):
    self.amount -= amount
    

  def display_user_balance(self):
    print(f"User: {self.name}, Balance {self.amount}")

  def transfer_money(self, amount, user):
    self.amount -= amount
    user.amount += amount
    self.display_user_balance()  
    user.display_user_balance()

rogan = User("Rogan")  
josh = User("Josh")
sara = User("Sara")


rogan.make_deposit(10)
rogan.make_deposit(20)
rogan.make_deposit(30)
rogan.make_withdrawlal(10)
rogan.display_user_balance()

josh.make_deposit(20)
josh.make_deposit(30)
josh.make_withdrawlal(10)
josh.make_withdrawlal(20)
josh.display_user_balance()

sara.make_deposit(100)
sara.make_withdrawlal(20)
sara.make_withdrawlal(10)
sara.make_withdrawlal(5)
sara.display_user_balance()


rogan.transfer_money(100, sara)