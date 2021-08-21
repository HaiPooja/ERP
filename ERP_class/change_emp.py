from emp_store import employees

def change_menu():
	print("\tPress 1. Change by name")
	print("\tPress 2. Change by age")
	print("\tPress 3. Change by salary")
	print("\tPress 4. Change by gender")
	print("\tPress 5. exit")


def change_main():
	while True:
		change_menu()
		choice=int(input("Enter your choice : "))
		if choice == 1:#change name
			e_id = input("Enter Employee id: ")
			st_temp  = list(filter(lambda a: a.e_id == e_id,employees))
			st_temp[0].set_name(input("Enter new name: "))
			
		elif choice == 2:#change age
			age = input("Enter age : ")
			st_temp  = list(filter(lambda a: a.age == age,employees))
			st_temp[0].set_age(input("Enter new age: "))
			
		elif choice == 3:#change salary
			salary = input("Enter salary : ")
			st_temp  = list(filter(lambda a: a.salary == salary,employees))
			st_temp[0].set_salary(input("Enter new salary: "))
			
		elif choice == 4:#gender
			gender = input("Enter gender : ")
			st_temp  = list(filter(lambda a: a.gender == gender,employees))
			st_temp[0].set_gender(input("Enter new gender: "))
		elif choice == 5:#exit
			break
		else:
			print("Invalid choice")
