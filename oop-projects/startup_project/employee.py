class Employee:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.earnings = 0

    def pay(self, amount):
        self.earnings += amount
        