from user import User
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

		
		employees.append(Employee())
		employees[-1].insert()


	elif choice == 2:#delete 
		eid=input("\nEnter the employye id:")
		for i in employees:
			if i.e_id == eid:
				employees.pop(employees.index(i))

	elif choice == 3:
		s.search_employee()
			
		
	elif choice == 4:
		for i in employees:
			i.display()
	elif choice == 5:
		c.change_main()
	elif choice == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")
