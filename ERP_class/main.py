from employee import Employee
from emp_store import employees
import employee as e
import search_emp as s
import change_emp as c

def main_menu():
	print("\nPress 1. Add employee")
	print("Press 2. Delete employee")
	print("Press 3. Search employee")
	print("Press 4. Display all employee")
	print("Press 5. Change a employee details") 
	print("Press 6. exit")

while True:
	main_menu()

	choice = int(input("Enter your choice : "))
	if choice == 1:

		e_id = input("\tEnter employee id : ")
		name = input("\tEnter name : ")
		age = input("\tEnter employee age : ")
		gender = input("\tEnter gender : ")
		place = input("\tEnter place : ")
		salary = input("\tEnter salary : ")
		previous_company = input("\tEnter previous company : ")
		joining_date = input("\tEnter joining_date : ")
		st_temp=Employee(e_id,name,age,gender,place,salary,previous_company,joining_date)
		e.employees.append(st_temp)


	elif choice == 2:#delete 
		eid=input("\nEnter the employye id:")
		for i in employees:
			if i.e_id == eid:
				employees.pop(employees.index(i))

	elif choice == 3:
		s.search_employee()
			
		
	elif choice == 4:
		for i in employees:
			print(f"{i.e_id} |{i.name} | {i.age} | {i.gender} | {i.place} | {i.salary}| {i.previous_company} | {i.joining_date}")
	elif choice == 5:
		c.change_main()
	elif choice == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")
