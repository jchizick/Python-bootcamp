class Category:

  def __init__(self,name):
   self.name = name
   self.ledger = []
  
  def deposit(self,amount,description=None):
    if description == None:
      self.ledger.append({'amount': (amount), 'description': ''})
    else:
      self.ledger.append({'amount': (amount), 'description': description})
  
  def withdraw(self,amount,description=None):
    if self.check_funds(amount) == True:
      if description == None:
        self.ledger.append({'amount': -(amount), 'description': ''})
      else:
        self.ledger.append({'amount': -(amount), 'description': description})
      return True
    else:
      return False

  def check_funds(self,amount):
    return amount <= self.get_balance()

  def get_balance(self):
    balance = 0
    for items in self.ledger:
      balance += items['amount']
    return balance
  
  def transfer(self,amount,budget_category):
    if self.check_funds(amount) == True:
      self.ledger.append({'amount': -(amount), 'description': f'Transfer to {budget_category.name}'})
      budget_category.deposit(amount, description = f'Transfer from {self.name}')
      return True
    else:
      return False

  def __str__(self): #print budget object
    name = self.name
    x = name.center(30,"*") #budget category title max 30 chars centred within *'s
    for items in self.ledger:
      txt = items['description'][:23] #only display the first 23 characters
      num = str("{:.2f}".format(items['amount'])) #two decimal places + max 7 chars
      x += f"\n{txt:<23}{num:>7}" #txt = left aligned , num = right aligned
    x += "\nTotal: "+ str(self.get_balance()) 
    return x

def create_spend_chart(categories):
  spendings = {} 
  for i in categories:
    x = 0
    for j in i.ledger:
      if j['amount']<0:
        x += j['amount']
    spendings[i.name] = round(x,2)
  total = sum(spendings.values()) #sum of spending per category

  percentage = {}
  for z in spendings.keys():
    percentage[z] = int(round(spendings[z]/total,2)*100) #total percentage spent by category
  
  output = 'Percentage spent by category\n' #printing chart
  for i in range(100,-10,-10):
    output += f'{i}'.rjust(3) + '| '
    for percent in percentage.values():
      if percent >= i:
        output += 'o  '
      else:
        output += '   '
    output += '\n'
  output += ' '*4+'-'*(len(percentage.values())*3+1)
  output += '\n     '

  keys_list = list(percentage.keys()) #splitting category name into letters
  max_chars = max([len(i) for i in keys_list])
  for i in range(max_chars):
    for name in keys_list:
      if len(name)>i:
        output += name[i] + '  '
      else:
        output += '   '
    if i < max_chars-1:
      output += '\n     '

   
  return output