
from user import User
from emp_store import employees
class Employee(User):
	def __init__(self):
		self.e_id = ""
		self.name = ""
		self.age = ""
		self.gender = ""
		self.place = ""
		self.salary = ""
		self.previous_company = ""
		self.joining_date = ""
		
	def insert(self):
		print("___________Add employee details____________")
		self.e_id = input("\tEnter employee id : ")
		self.name = input("\tEnter name : ")
		self.age = input("\tEnter employee age : ")
		self.gender = input("\tEnter gender : ")
		self.place = input("\tEnter place : ")
		self.salary = input("\tEnter salary : ")
		self.previous_company = input("\tEnter previous company : ")
		self.joining_date = input("\tEnter joining_date : ")
		self.set_username=(input("\tEnter user name : "))
		self.set_password=(input("\tEnter password : "))
		self._role=input("\tEnter user role : ")
		
	def display(self):
		print("____________________________________________Employee Details____________________________________________________")
		print(f"{self.e_id}=> {self.name} | {self.age} | {self.gender} | {self.place} | {self.salary}| {self.previous_company} | {self.joining_date}| {self.get_username} |{self.get_password}| {self._role} ")
	
	def set_name(self,name):
		self.name = name
		return "name assigned successfully"
	def set_age(self,age):
		self.age = age
		return "age assigned successfully"

	def set_gender(self,gender):
		self.gender = gender
		return "gender assigned successfully"
	def set_place(self,place):
		self.place = place
		return "place assigned successfully"
		
	def set_salary(self,salary):
		self.salary = salary
		return "salary assigned Successfully"
	
	def set_previous_company(self,previous_company):
		self.previous_company = previous_company
		return "Previous company assigned successfully"
	def set_joining_date(self,joining_date):
		self.joining_date = joining_date
		return "Joining date company assigned Successfully"
