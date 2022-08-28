#!/bin/python
#====================class=======================
class Employee:
		num_employees = 0
		raise_percent = 1.10
	#the first class created for basic functions
		def __init__(self, first, last, pay):
			#instance variables
			self.fname = first
			self.lname = last
			self.email = first + '.' + last + "@company.com"
			self.salary = pay
			#print('instance 1 inside class name in                ' + self.fname + self.lname)
			#print('instance 1 inside class email and pay is                ' + self.email + ', ' + str(self.salary))
			Employee.num_employees = Employee.num_employees + 1

		def fullname(self):
			return '{} {}'.format(self.fname, self.lname)

		def apply_raise(self):
			# appraisal will be 10 percent of the pay
			return self.salary * self.raise_percent

		@classmethod
		def set_raise_percent(cls, percent):
			cls.raise_percent = percent

		@classmethod
		def from_string(cls, emp_str):
			f, l, s = emp_str.split('-')
			print(cls(f, l, s)) #object is created
			return cls(f, l, s) #object is returned


emp_1 = Employee('sam','kurien',100)
emp_2 = Employee('winston','churchil',100)
emp_str3 = 'John-Doe-7000'


Employee.set_raise_percent(1.30)
emp_3 = Employee.from_string(emp_str3)


#emp_2.raise_percent = 1.20
print(Employee.raise_percent)
print(emp_1.raise_percent)
print(emp_2.raise_percent)

print(emp_1.salary)
print(emp_1.apply_raise())
print(emp_2.salary)
print(emp_2.apply_raise())
#print(emp_3.salary)
#print(emp_3.apply_raise())

#print(emp_3.salary)
print(emp_3)