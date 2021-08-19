from emp_store import org

def org_details():
	print("enter 1 for Add Organization")
	print("enter 2 for Edit Organization")
	print("enter 3 Display Organization details")
	print("enter 4 for exit")
	while True:
	
		choice = int(input("Enter choice : "))
		if choice == 1:
			add_oganization()
		elif choice == 2:
			edit_oganization()
		elif choice == 3:
			display_organization()
		elif choice == 4:
			break
		else:
			print("Invalid choice")	
def add_oganization():
	#add oraganization
	org['name']=input("enter organization name : ")
	org['email']=input("enter organization  email : ")

def edit_oganization():
	print("1 for Edit Organization name ")
	print("2 for Edit Organization email")
	choice = int(input("Enter choice: "))
	if choice == 1:
		org['name'] = input("enter new organization name :")
	elif choice == 2:
		org['email'] = input("enter new organization email : ")	
	else:
		print("invalid choice")
def display_organization():
	print(org)
