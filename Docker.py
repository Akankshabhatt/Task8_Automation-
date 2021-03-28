from os import system

def menu():
	# Docker menu loop
	while True:
		system("clear")
		system("tput setaf 2")
		print("\n\t"+42*"-")
		print("\t\t\tDocker Menu")
		print("\t"+42*"-")
		system("tput setaf 3")
		print("\n\tPlease select an option: \n")
		system("tput setaf 5")
		print("\t\t1 : Install docker")
		print("\t\t2 : Start docker service")
		print("\t\t3 : Stop docker service")
		print("\t\t4 : View docker info")
		print("\t\t5 : View active containers")
		print("\t\t6 : View all containers")
		print("\t\t7 : View downloaded images")
		print("\t\t8 : Pull an image")
		print("\t\t9 : Launch a container")
		print("\t\t10 : Stop a container")
		print("\t\t11 : Start a container")
		print("\t\t12 : Remove an image")
		print("\t\t13 : Remove a container")
		print("\t\t0 : Previous menu")
		
		system("tput setaf 6")
		opt = input("\n\tOption selected: ")
		system("tput setaf 7")

		# Install Docker
		if opt == '1':
			system("clear")
			if not system("rpm -q docker-ce"):
				print("\tDocker is already installed. Exiting installation...")
				system("sleep 2")
				
			else:
				print("\tInstalling Docker...")
				
				f = open("/etc/yum.repos.d/docker-ce_install.repo","a")
				dockrepo = "[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0\n"
				f.write(dockrepo)
				f.close()
			system("yum install docker-ce --nobest")
			system("systemctl enable docker")
			system("systemctl start docker")
			system("sleep 2")
		# Start docker service
		elif opt == '2':
			system("clear")
			system("systemctl start docker")

		# Stop docker service
		elif opt == '3':
			system("clear")
			system("systemctl stop docker")

		# View docker info
		elif opt == '4':
			system("clear")
			cmd = "docker info | less"
			system(cmd)
			
		# View active containers
		elif opt == '5':
			system("clear")
			cmd = "docker ps | less"
			system(cmd)
			
		# View all containers
		elif opt == '6':
			system("clear")
			cmd = "docker ps -a | less"
			system(cmd)
			
		# View downloaded images
		elif opt == '7':
			system("clear")
			cmd = "docker images | less"
			system(cmd)
			
		# Pull an image
		elif opt == '8':
			system("clear")
			system("tput setaf 6")
			img = input("\n\tEnter image name: ")
			ver = input("\tEnter image version (optional): ")
			system("tput setaf 7")
			
			if img:
				cmd = f"docker pull {img}:{ver}" if ver != "" else f"docker pull {img}"
				system(cmd)
				system("sleep 2")
				break
			else:
				print("\n\tNo image name entered! Getting back to previous menu...\n")
				system("sleep 2")

		# Launch a container
		elif opt == '9':
			system("clear")
			flags = ""
			system("tput setaf 6")
			img = input("\tEnter image name: ")
			ver = input("\tEnter image version (optional): ")
			interact = input("\tInteractive (y/n): ")
			console = input("\tShell prompt (y/n): ")
			name = input("\tEnter container name (optional): ")
			system("tput setaf 7")
			
			if img:
				if interact or console:
					flags += '-'
					if interact.lower() in ['y','yes']: flags += 'i'
					if console.lower() in ['y','yes']: flags += 't'
				if name: flags += f" --name {name}"
			
				cmd = f"docker run {flags} {img}:{ver}" if ver else f"docker run {flags} {img}"
				system(cmd)
				
			else: print("\tPlease enter an image name!")
			system("sleep 2")
			
		# Stop a container
		elif opt == '10':
			system("clear")
			system("tput setaf 6")
			name_id = input("\tEnter container name or id: ")
			system("tput setaf 7")
			system(f"docker stop {name_id}") if name_id else print("\tPlease enter a container name/ID!")
			system("sleep 2")

		# Start a container
		elif opt == '11':
			system("clear")
			name_id = input("\tEnter container name or ID: ")
			system(f"docker start {name_id}") if name_id else print("\tPlease enter a container name/ID!")
			system("sleep 2")
			
		# Remove an image
		elif opt == '12':
			system("clear")
			flags,img = "",""
			system("tput setaf 6")
			img = input("\tEnter image name: ")
			ver = input("\tEnter image version (optional): ")
			force = input("\tForce remove (y/n): ")
			system("tput setaf 7")
			
			if force.lower() in ['y', 'yes']: flags += "--force"
			if img:
				cmd = (f"docker rmi {img}:{ver} {flags}" if ver != "" else f"docker rmi {img} {flags}")
				system(cmd)
			else:
				system("clear")
				print("\tPlease enter an image name!")
				
			system("sleep 2")
			
		# Remove a container
		elif opt == '13':
			system("clear")
			system("tput setaf 6")
			name_id = input("\tEnter container name or ID: ")
			system("tput setaf 7")
			system(f"docker rm {name_id}") if name_id else print("\tPlease enter a container name/ID!")
			system("sleep 2")

		# Previous menu	
		elif opt == '0':
			system("clear")
			break
			
		else:
			system("clear")
			print("\tPlease enter a valid option!\n")
			system("sleep 2")
			
