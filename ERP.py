#start a mini project console ERP system.
employees={}
teams={}
def main_menu():
	print("Press 1 for add employee")
	print("Press 2 for delete employee ")
	print("Press 3 for search employee")
	print("Press 4 for display  employee")
	print("Press 5 for change employee details")
	print("press 6 for manage all team")
	print("Press 7 for Quit")

def add_employee():
	employee_id = int(input("\tenter Employee id "))
	if employee_id not in employees.keys():
		name = input("\tenter name ")
		age = int(input("\tenter age "))
		gender = input("\tenter the gender ")
		place = input("\tenter place ")
		salary = int(input("\tenter salary "))
		previous_company = input("\tenter your previous company ")
		joining_date = input("\tenter joining date ")
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
	eid = int(input("\tEnter employee id"))
	if eid not in employees.keys():
		print("\tWrong Employee id")
	else:
		del employees[eid]

def search_employee():
	name = input("\tEnter name")
	found = False
	for i in employees.values():
		if i["name"] == name: 
			print(f"\t{i['name']} | {i['age']} | {i['place']} | {i['gender']} | {i['previous_company']} | {i['salary']} ")
			found = True
			break
		if found==False:
			print("\tnot in the list")

def display_employee():
	for id,employee in employees.items():
		print(f"\t{id} | {employee['name']} | {employee['age']} | {employee['place']} | {employee['gender']} | {employee['previous_company']} | {employee['salary']} ")

def change_employee():
	print("Enter 1 for change name")
	print("Enter 2 for change age")
	print("Enter 3 for change gender")
	print("Enter 4 for change salary")
	cho =int(input("\tEnter your choice."))
	employee_id = input("\tEnter employee id.")
	if cho == 1:
		employees[employee_id]['name'] = input("\tEnter new name") 
	elif cho == 2:
		employees[employee_id]['age'] = int(input("\tEnter new age"))
	elif cho == 3:
		employees[employee_id]['gender'] = input("\tEnter gender")
	elif cho == 4:
		employees[employee_id]['salary'] = int(input("\tEnter new salary"))
	else:
		print("invalid")
def manage_all_team_menu():
	print("\t press 1. create team ")
	print("\t press 2. Display team ")
	print("\t press 3. manage team ")
	print("\t press4. Delete team ")
	print("\t press5. exit ")
def manage_all_team():
	while True:
		manage_all_team_menu()
		ch=int(input("enter your choice"))
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
	team_name=input("\tEnter team name")
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
		team_name=input("\t\t Enter team name ")
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
	display_employee()
	eid=int(input("\t\t Enter the employee id of employee "))
	if eid in employees.key():
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
		name_string=name_string +"|"+i+"."+employee[i]["name"]
	print(f"{name_string}")	


while True:
	main_menu()
	ch=int(input("enter your choice"))
	if ch == 1:
	#adding employee
		add_employee()
			
	elif ch == 2:
	#delete
		delete_employee()
	elif ch == 3:
	#search
		search_employee()
	elif ch == 4:
	#display employee
		display_employee()
	elif ch== 5:
	#change employee details
		change_employee()
	elif ch==6:
	#manage all team
		manage_all_team()
	elif ch == 7:
		break;
	else:
		print("Invalid Choice")



