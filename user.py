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