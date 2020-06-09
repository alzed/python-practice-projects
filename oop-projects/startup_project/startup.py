from employee import Employee

class Startup:
    def __init__(self, name, funding, salaries):
        self.name = name
        self.salaries = salaries
        self.funding = funding
        self.employees = []

    def is_valid_title(self, title):
        return title in self.salaries

    def hire(self, name, title):
        if self.is_valid_title(title):
            self.employees.append(Employee(name, title))

    def size(self):
        return len(self.employees)

    def payday(self):
        for employee in self.employees:
            salary = self.salaries[employee.title]
            employee.pay(salary)
            self.funding -= salary

    def average_salary(self):
        sum_salaries = sum([self.salaries[employee.title] for employee in self.employees])
        return sum_salaries/len(self.employees)

    def close(self):
        self.employees = []
        self.funding = 0

    def acquire(self, startup):
        self.funding += startup.funding
        for title, salary in startup.salaries.items():
            if title not in self.salaries:
                self.salaries[title] = salary

        for employee in startup.employees:
            self.hire(employee.name, employee.title)

        startup.close()
    