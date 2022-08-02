class Employee:
    raise_amt = 1.04
    num_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_employee += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees==None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())


emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

mgr = Manager("Soo", "Smith", 90000, [emp1])

print(repr(emp1))
print(emp1+emp2)

"""import datetime
my_date = datetime.date(2016, 7, 16)
print(Employee.is_workday(my_date))"""

"""emp_str_1 = "Elon-Musk-70000"
emp_str_2 = "Steve-Jobs-30000"
emp_str_3 = "Jane-Doe-90000"
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)"""



