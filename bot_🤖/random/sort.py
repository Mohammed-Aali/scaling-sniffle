class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:
        return '{}, {}, ${}'.format(self.name, self.age, self.salary)

e1 = Employee('Mohammed', 24, 200000)
e2 = Employee('Ali', 15, 10000)
e3 = Employee('Yousef', 7, 2000)

employees = [e1, e2, e3]

s_employees = sorted(employees, key=lambda x: x.age)

print(s_employees)