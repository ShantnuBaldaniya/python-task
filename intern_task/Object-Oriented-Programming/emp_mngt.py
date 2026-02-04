class Employee:
    def __init__(self, name, department, salary, emp_id):
        self.name = name
        self.department = department
        self.salary = salary
        self.id = emp_id

    def get_raise(self, amount):
        self.salary += amount
        return f" New salary is: {self.salary}"

    def get_details(self):
        return f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}, ID: {self.id}"

class Developer(Employee):
    def __init__(self, name, department, salary, emp_id, languages=None):
        super().__init__(name, department, salary, emp_id)
        self.languages =  []

    def add_language(self, lang):
        self.languages.append(lang)

    def calculate_bonus(self):
        return self.salary * 0.12

    def display_details(self):
        return f"the details is :{self.name}, {self.department}, {self.salary}, {self.id}, Languages: {', '.join(self.languages)}"




e=Employee('shantnu','python',4500,90)
d=Developer('x','c',344,3,'c++')
print(e.get_raise(2))
print(d.display_details())
print(d.add_language('python'))
print(d.display_details())