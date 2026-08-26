# class shape:
#     def area(self):
#         print("Area of shape"
#               )
# class rectangle(shape): 
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         print("Area of rectangle:", self.length * self.breadth)   
        
# class circle(shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print("Area of circle:", 3.14 * self.radius * self.radius)  
# c=circle(5)
# r=rectangle(4, 6)
# c.area()
# r.area()                


# class payment:
#     def amount(self):
#         print("Payment method")
# class cash(payment):
#     def amount(self):
#         print("Payment by cash")
# class upi(payment):
#     def amount(self):
#         print("Payment by UPI")    
        
        
# c=cash()
# u=upi()
# c.amount()
# u.amount()                    

class employee:
    def calculate_salary(self):
        print("Salary of employee")
class full_time_employee(employee):
    def calculate_salary(self, salary):
        self.salary = salary
        print("Salary of full-time employee")
class part_time_employee(employee):
    def calculate_salary(self, salary):
        self.salary = salary
        print("Salary of part-time employee")
class contract_employee(employee):
    def calculate_salary(self, salary):
        self.salary = salary
        print("Salary of contract employee") 
    def __init__(self, salary):
        self.salary = salary    
fe=full_time_employee()
pe=part_time_employee()
ce=contract_employee()
fe.calculate_salary(450000)
pe.calculate_salary(20000)
ce.calculate_salary(100000) 
print("Full-time employee salary:", fe.salary)
print("Part-time employee salary:", pe.salary)
print("Contract employee salary:", ce.salary)                              