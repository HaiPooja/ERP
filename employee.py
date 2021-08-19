from emp_store import employees

def main_menu():
	print("\nPress 1 for add employee")
	print("Press 2 for delete employee ")
	print("Press 3 for search employee")
	print("Press 4 for display  employee")
	print("Press 5 for change employee details")
	print("press 6 for manage all team")
	print("Press 7 for exit from this loop")

def add_employee():
	employee_id = int(input("\tenter Employee id: "))
	if employee_id not in employees.keys():
		name = input("\tenter name: ")
		age = int(input("\tenter age : "))
		gender = input("\tenter the gender: ")
		place = input("\tenter place : ")
		salary = int(input("\tenter salary :"))
		previous_company = input("\tenter your previous company :")
		joining_date = input("\tenter joining date: ")
		temp ={
			"name":name,
			"age":age,
			"gender":gender,
			"place":place,
			"salary":salary,
			"previous_company":previous_company,
			"joining_date":joining_date,
			}
		employees[employee_id] = temp
	else:
			print("\tEmployee id  already Taken")

def delete_employee():
	eid = int(input("\tEnter employee id: "))
	if eid not in employees.keys():
		print("\tWrong Employee id: ")
	else:
		del employees[eid]

def search_employee():
	
	print("Press 1 for search by name")
	print("Press 2 for search by age")
	print("Press 3 for search by salary")
	print("Press 4 for search  by gender")
	print("Press 5 for exit")
	while True:
	
		choice = int(input("Enter choice : "))
		if choice == 1:
			search_by_name()
		elif choice == 2:
			search_by_age()
		elif choice == 3:
			search_by_salary()
		elif choice == 4:
			search_by_gender()
		elif choice == 5:
			break
		else:
			print("Invalid choice")
def search_by_name():	
	name=input("Enter the name: ")
	print(list(filter(lambda a:a["name"] == name, employees.values())))
	print("We Found")

def search_by_age():	
	age=int(input("Enter the age : "))
	print(list(filter(lambda a:a["age"] == age, employees.values())))
	print("We Found")

def search_by_salary():	
	salary=int(input("Enter the salary : "))
	print(list(filter(lambda a:a["salary"] == salary, employees.values())))
	print("We Found")

def search_by_gender():	
	gender=input("Enter the gender : ")
	print(list(filter(lambda a:a["gender"] == gender, employees.values())))
	print("We Found")

def display_employee():
	for id,employee in employees.items():
		print(f"\t{id} | {employee['name']} | {employee['age']} | {employee['place']} | {employee['gender']} | {employee['previous_company']} | {employee['salary']} ")

def change_employee():
	print("Enter 1 for change name")
	print("Enter 2 for change age")
	print("Enter 3 for change gender")
	print("Enter 4 for change salary")
	cho =int(input("\tEnter your choice : "))
	employee_id = input("\tEnter employee id : ")
	if cho == 1:
		employees[employee_id]['name'] = input("\tEnter new name: ") 
	elif cho == 2:
		employees[employee_id]['age'] = int(input("\tEnter new age: "))
	elif cho == 3:
		employees[employee_id]['gender'] = input("\tEnter gender: ")
	elif cho == 4:
		employees[employee_id]['salary'] = int(input("\tEnter new salary: "))
	else:
		print("invalid")

