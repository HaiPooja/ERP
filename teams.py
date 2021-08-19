from emp_store import teams
from emp_store import employees
import employee as e

def manage_all_team_menu():
	print("\t press 1. create team ")
	print("\t press 2. Display team ")
	print("\t press 3. manage team ")
	print("\t press4. Delete team ")
	print("\t press5. exit ")
def manage_all_team():
	while True:
		manage_all_team_menu()
		ch=int(input("enter your choice : "))
		if ch == 1:
		#create team
                	create_team()
		elif ch == 2:
		#display team
                	display_team()
		elif ch == 3:
		#manage team
                	manage_team()
		elif ch == 4:
		#delete team
                	delete_team()
		elif ch== 5:
		#exit
			break;
		else:
			print("invalid option")
def create_team():
	team_name=input("\tEnter team name : ")
	teams[team_name]=[]
	
def display_team():
	for key,value in teams.items(): 
		name_string = ""
		for i in value:
			name_string = name_string +"|"+employees[i]["name"]
		print(f"{key} => {name_string}")
	
def delete_team():
	team_name=input("\tEnter team name ")
	if team_name in teams.keys():
		del teams[team_name]
		print("\t Deleted the  team ")
	else:
		print("\t incorrect name ")
def manage_team_menu():
	print("\t press 1. Add member ")
	print("\t press 2. Delete member ")
	print("\t press 3. Display member list ")
	print("\t press 4. Exit")
def manage_team():
	while True:
		team_name=input("\t\t Enter team name : ")
		manage_team_menu()
		ch=int(input("enter your choice"))
		if ch == 1:
                #Add member
			add_member(team_name)
		elif ch == 2:
                #Delete member
                        delete_member(team_name)
		elif ch == 3:
                #Display
			display_member(team_name)
		elif ch==4:
		#exit
			break
		else:
			print("\tinvalid")
def add_member(team_name):
	e.display_employee()
	eid=int(input("\t\t Enter the employee id of employee "))
	if eid in e.employees.keys():
		teams[team_name].append(eid)
	else:
		print("\t\t wrong eid")

def delete_member(team_name):
	display_member(team_name)
	employee_id=int(input("\t\tEnter the employee id "))
	if employee_id in teams[team_name]:
		teams[team_name].remove(employee_id)
	else:
		print("\t\twrong id")

def display_member(team_name):
	name_string=""
	for i in teams[team_name]:
		name_string=name_string +"|"+str(i)+"."+e.employees[i]["name"]
	print(f"{name_string}")


