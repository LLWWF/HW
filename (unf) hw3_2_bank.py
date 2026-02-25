categories = []
class Transaction():
    def __init__(self, data, amount, category, ttype, categories=categories):
        self.data  = data
        self.amount = amount
        self.category = category if category in categories else categories.append(category), self.category = category
        self.ttype = ttype
    def info(self):
        return {
        'data'  : self.data,
        'category' : self.category,
        'type' : self.ttype,
        'amount' : self.amount
        }
class Category():
    def __init__(self, name, budget:int, categories=categories):
        self.name = name
        self.budget = 0 + budget
        categories.append(self)

