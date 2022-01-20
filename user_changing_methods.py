class User:

  def __init__(self, name):
    self.name = name
    self.amount = 0

  def make_deposit(self, amount):
    self.amount += amount
    return self
    

  def make_withdrawlal(self, amount):
    self.amount -= amount
    return self
    

  def display_user_balance(self):
    print(f"User: {self.name}, Balance {self.amount}")
    return self
    

  def transfer_money(self, amount, user):
    self.amount -= amount
    user.amount += amount
    self.display_user_balance()  
    user.display_user_balance()
    return self

rogan = User("Rogan")  
josh = User("Josh")
sara = User("Sara")


rogan.make_deposit(10).make_deposit(20).make_deposit(30).make_withdrawlal(10).display_user_balance()

josh.make_deposit(20).make_deposit(30).make_withdrawlal(10).make_withdrawlal(20).display_user_balance()

sara.make_deposit(100).make_withdrawlal(20).make_withdrawlal(10).make_withdrawlal(5).display_user_balance()


rogan.transfer_money(100, sara)