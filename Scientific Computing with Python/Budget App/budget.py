import math

def rounddown(x):
    return int(math.floor(x / 10.0)) * 10


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description='', budget_category=None):
        if budget_category:
            budget_category.ledger.append({"amount": amount, "description": description})
        else:
            self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        balance = 0
        for money in self.ledger: # calculate total
            balance += money['amount']
        return balance

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def withdraw(self, amount, description='', budget_category=None):
        if self.check_funds(amount):
            self.ledger.append({"amount": -abs(amount), "description": description}) # -abs makes number negative
            return True
        else:
            return False

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, description=f'Transfer to {budget_category.name}')
            budget_category.deposit(amount, description=f'Transfer from {self.name}', budget_category=budget_category)
            return True
        else:
            return False

    def __str__(self):
        string = str(self.name).center(30, '*') + '\n'
        for item in self.ledger:
            description = list(item['description'][:30].ljust(30))
            length = len(str(format((item['amount']), '.2f'))) - 1
            for i in range(len(str(format((item['amount']), '.2f')))):
                amount = format((item['amount']), '.2f')
                description[29 - (length - i)] = str(amount)[i]
            description[29 - (length + 1)] = " "
            string += ''.join(description) + '\n'
        string += f'Total: {self.get_balance()}'
        return string

def create_spend_chart(category_list):
    spending_absolute = {} # a dict that stores the $ spend per category
    spending_percent = {} # a dict that stores the % $ spend per category
    max_len_category_name = 0 # the length of the longest category name
    total_spend = 0
    for category in category_list:
        category_spending = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                total_spend += transaction['amount']
                category_spending += transaction['amount']
        spending_absolute[category.name] = category_spending
    for category in spending_absolute:
        spending_percent[category] = (spending_absolute[category] / total_spend) * 100 # calculate the % spend per category
        if len(category) > max_len_category_name: # finding the longest category name
            max_len_category_name = len(category)
    string = ""
    string += "Percentage spent by category\n"
    for i in reversed(range(0, 101, 10)): # plotting the chart part
        string += f"{i:>3}|"
        for category in spending_percent:
            perc = rounddown(spending_percent[category])
            if perc >= i:
                string += " o "
            else:
                string += "   "
        string += " \n"
    string += "    -"
    string += "---" * len(spending_percent)
    string += '\n'
    for index in range(0, max_len_category_name):
        string += "     "
        for category in spending_percent:
            try:
                string += category[index] + "  "
            except IndexError:
                string += "   "
        if index != max_len_category_name - 1:
            string += '\n'
    return string