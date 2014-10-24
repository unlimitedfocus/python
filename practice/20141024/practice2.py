class MyClass:
    '''
        a simple example class
    '''
    i = 12345
    def f(self):
        return 'hello world'

    def __init__(self):
        self.data = []

x = MyClass()
print x.f()

xf = x.f
print xf()

class Employee:
    pass

    def show(self):
        print self.name, self.dept, self.salary


john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

john.show()

# raise Employee

import os

print os.getcwd()
os.chdir('..')
print os.getcwd()
os.chdir('20141024')
print os.getcwd()


help(os)

