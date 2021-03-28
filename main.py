from getpass import getpass
from os import system

PW = "pw"

while True:
	system("tput setaf 6")
	pw = getpass("\n\tTo continue, please enter your password: ")
	if pw == PW:
		system("tput setaf 2")
		print("\n\tUser authenticated! Proceeding with the program...")
		system("sleep 1")
		break
	else:
		system("tput setaf 1")
		print("\tIncorrect password!\n")

while True:
	while True:
		system("clear")
		system("tput setaf 2")
		print("\n\t"+48*"-")
		system("tput setaf 6")
		print("\t\tARTH Team 12.7 Automation Menu")
		system("tput setaf 2")
		print("\t"+48*"-")
		system("tput setaf 3")
		print("\n\tNote: To get the best out of this program, please ensure that you have AppStream and BaseOS repositories present in your RHEL 8 system.")
		system("tput setaf 7")
		print("\n\tPlease select an option: \n")
		system("tput setaf 5")
		print("\t\t1 : Shell prompt")
		print("\t\t2 : Docker")
		print("\t\t3 : AWS")
		print("\t\t4 : Hadoop")
		print("\t\t5 : RHEL 8 Utilities")
		print("\t\t6 : Install Apache Web Server")
		print("\t\t0 : Exit")
		
		system("tput setaf 6")
		opt = input("\n\tOption selected: ")
		system("tput setaf 7")
		
		if opt == '1':
			local = True
			while True:
				inp = input("\n\tLocal (l) or Remote (r) prompt? :")
				if inp.lower() in ['r', 'remote']:
					local = False
					break
				elif inp.lower() in ['l', 'local']: break
				else: print("\tPlease enter either (l / local) or (r / remote)!\n")
			if local:
				user = input("\n\tEnter your username on this system: ")
				system(f"ssh {user}@localhost")
			else:
				system("tput setaf 6")
				ip = input("Enter remote IP: ")
				user = input("Enter remote username: ")
				system("tput setaf 7")
				system(f"ssh {user}@{ip}")
			
		elif opt == '2':
			import Docker
			system("clear")
			Docker.menu()
			
		elif opt == '3':
			import AWS
			system("clear")
			AWS.menu()
			    
		elif opt == '4':
			import Hadoop
			system("clear")
			Hadoop.menu()
			
		elif opt == '5':
			system("clear")
			import RHEL8_Utils
			RHEL8_Utils.menu(PW)
			
		elif opt == '6':
			system("clear")
			local = True
			while True:
				system("tput setaf 6")
				inp = input("\n\tLocal (l) or Remote (r) install? :")
				system("tput setaf 7")
				if inp.lower() in ['r', 'remote']:
					local = False
					break
				elif inp.lower() in ['l', 'local']: 
					system("yum install httpd")
					system("sleep 2")
					break
				else: print("\tPlease enter either (l / local) or (r / remote)!\n")
			if not local:
				system("tput setaf 6")
				ip = input("\tEnter remote IP: ")
				user = input("\tEnter remote username: ")
				system("tput setaf 7")
				system(f"ssh {user}@{ip} yum install httpd")
				system("sleep 2")
			
		elif opt == '0':
			exit()
			
		else:
			pass
