#start a mini project console ERP system.
#creating modules


import teams as t
import organization as o
import employee as e
from emp_store import employees
from emp_store import teams
from emp_store import org 




	
while True:
	o.org_details()
	#first organization details 
	e.main_menu()
	ch=int(input("enter your choice: "))
	if ch == 1:
	#adding employee
		e.add_employee()
			
	elif ch == 2:
	#delete
		e.delete_employee()
	elif ch == 3:
	#search
		e.search_employee()
	elif ch == 4:
	#display employee
		e.display_employee()
	elif ch== 5:
	#change employee details
		e.change_employee()
	elif ch==6:
	#manage all team
		t.manage_all_team()
	elif ch == 7:
		break;
	else:
		print("Invalid Choice")



