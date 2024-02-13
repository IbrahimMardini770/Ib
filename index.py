# class Employee:
#     def __init__(self):
#         print("employee created")

#     def __del__(self):
#         print("Destrucotr called")


# def create_obj():
#     print('making object...')
#     obj=Employee()
#     print('function end....')
#     return obj

# print('calling create_obj( function...)')
# obj=Employee()
# print('program end....')

# class RecursiveFunction:
# 	def __init__(self, n):
# 		self.n = n
# 		print("Recursive function initialized with n =", n)

# 	def run(self, n=None):
# 		if n is None:
# 			n = self.n
# 		if n <= 0:
# 			return
# 		print("Running recursive function with n =", n)
# 		self.run(n-1)

# 	def __del__(self):
# 		print("Recursive function object destroyed")

# # Create an object of the class
# obj = RecursiveFunction(5)

# # Call the recursive function
# obj.run()

# # Destroy the object
# # del obj


# A Python program to demonstrate inheritance
class Person(object):

# Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)


# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()
