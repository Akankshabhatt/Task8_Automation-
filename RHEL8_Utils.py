#Importing Libraries
import os #to run OS related commands
import getpass #For making password secure while typing

def menu(PW):
	#ALL FUNCTIONS
	#---------------------------------------
	#F1
	#To handle INCORRECT USER INPUT
	def incorr():
		os.system("tput setaf 1")
		os.system("clear")
		print("\n\n\n\n\n\t\t\t\tSeems Alien to me 8-(\n")
		os.system("sleep 2")
		os.system("clear")
		print("\n\n\n\n\n\t\t\t\tReconnecting......")
		os.system("sleep 1")
		os.system("clear")
		choose() #Direct to Choice Page
	#F2	
	#CONTINUE OR EXIT from the program
	def choose():
		os.system("sleep 1")
		os.system("tput setaf 2")
		choice=input("\n\t\tC --> to Continue/Restart\n\t\tE --> to Exit \n\t\t\t")
		os.system("tput setaf 0")
		#TO check user input :
		if choice in ["C", 'c']:
			os.system("clear")
			#menu display and take user's choice
			m=menuprint()
			#proceed w.r.t. choice
			proceed(m)
		elif choice in ["E","e"]:
			os.system("tput setaf 7")
			exit() #Exit from python program
		else:
			incorr()#Directed to incorrect input handling function
	#F3		
	#RHEL MENU PRINT--> MAIN PART OF THE CODE!!!!
	def menuprint():
		os.system("clear")
		os.system("tput setaf 39")
		#Print the menu
		print('''RHEL MENU :\n
		F --> Firewall Menu\n
		Y --> Yum Menu\n
		U --> User Menu\n
		P --> Partitioning Menu\n''')
		os.system("tput setaf 241")
		#take input from user
		m=input("Enter your choice : ")
		return m.lower()
	#F4
	#Proceed w.r.t choice--> TO REDIRECT TO RESPECTIVE FNCTION according to choice entered by user
	def proceed(m):
		os.system("clear")
		if m=="f":
			firewall()
		elif m=="y":
			yum()
		elif m=="u":
			user()
		elif m=="p":
			partition()
		else:
			incorr()
	#------------
	#MENU-F1--->>>FIREWALL
	def firewall():
		os.system("tput setaf 5")
		print('''FIREWALL MENU
		1 --> to Start
		2 --> to Stop
		S --> to check Status of Firewall''')
		ed=input("Enter your choice : ")
		os.system("tput setaf 0")
		#STOP FIREWALL
		if ed=="2":
			os.system("systemctl stop firewalld") #Stop firewall temporarily
			print("Firewall Stopped ")
		#START FIREWALL
		elif ed=="1":
			os.system("systemctl start firewalld") #Start firewall temporarily
			print("Firewall Started ")
		#STATUS FIREWALL
		elif ed.upper()=="S":
			print("Status : \n(Press q to exit)\n")
			print(os.system("systemctl status firewalld")) #to print current status of firewall service
		else:
			incorr()
		choose() #direct to user choice input function
	#MENU-F2--->>>YUM
	def yum():
		os.system("tput setaf 136")
		print('''YUM MENU
		A --> to ADD new repository
		D --> to DELETE existing repository
		L --> to LIST all existing repositories
		R --> reload all repositories
		V --> view any repo
		''')
		ed=input("Enter your choice : ")
		ed=ed.lower()
		os.system("tput setaf 125")
		#ADD NEW REPO
		if ed=="a":
		    #Taking inputs from user
			reponame = input("Enter repository name : ")
			baseurl = input("Enter BaseURL : ")
			gpg = input("GPGCHECK = 0/1 ? -> ")
			#writing the user inputs in a file
			#the file will be created in repository location of yum
			file = open(f"/etc/yum.repos.d/{reponame}.repo","a")
			filestr = f"[{reponame}]\nbaseurl={baseurl}\ngpgcheck={gpg}\n"
			file.write(filestr+'\n')
			file.close()
			#To view the created repo
			os.system("tput setaf 1")
			print("\n\nRepo creation under process........")
			os.system("sleep 1")
			os.system("clear")
			print("Your repo is as follows : ")
			os.system("tput setaf 7")
			os.system("cat /etc/yum.repos.d/{}.repo".format(reponame))
			os.system("sleep 2")
			choose()
		#DELETE REPO
		elif ed=="d":
			print("List of existing repositories : ")
			os.system("ls /etc/yum.repos.d/")
			reponame=input("Enter the repository you wanna delete : ")
			os.system("rm -f /etc/yum.repos.d/{}".format(reponame))
			print("Your repo has been deleted\nList of remaining repositories : \n")
			os.system("ls /etc/yum.repos.d/")
			choose()
		#List all existing REPOs
		elif ed=="l":
			print("List of existing repositories is : \n  ")
			os.system("ls /etc/yum.repos.d/")
			choose()
		#Reload REPOs
		elif ed=="r":
			print("Reloading all the repositories....\n ")
			os.system("yum repolist")
			choose()
		elif ed=="v":
			print("List of existing repositories : \n")
			os.system("ls /etc/yum.repos.d/")
			reponame=input("\nEnter the repository you wanna view : ")
			os.system("tput setaf 90 ")
			os.system("cat /etc/yum.repos.d/{}".format(reponame))
			choose()	
		else:
			incorr()
	#MENU-F3--->>>USER
	def user():
		os.system("tput setaf 166")
		print('''USER MENU
		A --> to ADD new user
		D --> to DELETE existing user
		L --> to LIST all existing users
		''')
		ed=input("Enter your choice : ")
		ed=ed.lower()
		os.system("tput setaf 5")
		#Add new user
		if ed=="a":
			uname=input("Enter new username : ")	
			os.system("useradd {}".format(uname))
			os.system("passwd {}".format(uname))
			print("\nUser added Successfully..!")
		#delete existing user
		elif ed=="d":
			uname=input("Enter username to be deleted : ")	
			os.system("userdel -rf {}".format(uname))
			print("\nUser deleted Successfully..!")
		#list all users
		elif ed=="l":
			print("List of existing Users is as follows :\n")
			os.system("ls /home")#printing the contents of the directory which contains folders of each user
		else:
			incorr()	
		choose()
	#MENU-F4--->>>PARTITION
	def partition():
		os.system("tput setaf 125")
		print('''PARTITION MENU
		L --> to List existing Partitions
		C --> to Create new partition
		F --> to Format a partition
		M --> to Mount a partition
		''')
		ed=input("Enter your choice : ")
		ed=ed.lower()
		os.system("tput setaf 7 ")
		#List of Existing Partitions
		if ed=="l":
			print("List of Existing Partitions :")
			os.system("df -h")
		#to Mount a partition
		elif ed=="m":
			mountpoint=input("Enter name for the Mount point")
			os.system("mkdir {}".format(mountpoint))
			print("Mountpoint created with the name : ",mountpoint)
			print("List of existing partitions : ")
			os.system("df -h")
			os.system("tput setaf 7 ")
			part=input("Enter the name of partition to be mounted : ")
			os.system("mount {} {}".format(part,mountpoint))
			print("Mounting Successful\nCheck below :")
			os.system("df -h")
		#to Format a partition
		elif ed=="f":
			print("List of existing partitions : ")
			os.system("df -h")
			os.system("tput setaf 7 ")
			part=input("Enter the name of partition to be Formatted : ")
			os.system("mkfs.ext4 {}".format(part))
			print("Formatting Successful.!")
		#to Create new partition
		elif ed=="c":
			print("Choose among the existing Disks: ")
			os.system("fdisk -l")
			os.system("tput setaf 7 ")
			disk=input("Enter the disk in which you wanna create partition and proceed as directed\n")
			os.system("fdisk {}".format(disk))
			os.system("tput setaf 7 ")
			print("Partition Created Successfully\nVerify from the following list :")
			os.system("df -h")
		else:
			incorr()
		choose()
	#------------------------------------------
	#------------------------------------------
	#BODY OF THE PROGRAM -->>>LOGIN
	os.system("clear")
	os.system("tput setaf 241")
	name=input("Enter Username : ")
	passwd=getpass.getpass("Enter Password : ")
	#User Authentication
	if passwd!=PW:
		os.system("tput setaf 1")
		print("You are not authorized to access this menu")
		os.system("tput setaf 7")
		exit()
	else:#In case password is correct
		os.system("clear")
		os.system("tput setaf 125")
		print("\t\t\tWELCOME ",name.upper())
		os.system("tput setaf 3")
		print("This is your RHEL Portal")
		os.system("tput setaf 3")
		print("------------------")
		choose()#redirected to choose function to take input from user
	os.system("tput setaf 7")
