class Employee: #Create class(blueprint)
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def  fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schofer', 50000  ) #Create instance of class
emp_2 = Employee('Korey','Test', 60000) #Create instance of class

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())
