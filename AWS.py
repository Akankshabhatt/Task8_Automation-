# aws section of menu driven program
# written by vinay prakash jadhav ARTH20-team12.7 for task8

# To use this code call the check_requirements() in the main menu driven program while integrating the code and remove the if __name__ == "__main__"

# this program can perform following functions:
# install aws cli on your system if required
# configure aws cli
# create a key-pair and save it on system
# Create a new aws instance
# Start a aws instance
# Describe ec2 instance
# Create a EBS volume
# Attach a EBS volume to ec2 instance
# Create s3 bucket
# Upload a file in bucket
# Create a distribution in aws CloudFront

#importing os to get system() so that we can execute aws configure command

import os

#importing subprocess to get access to getstatusoutput() so that we can execute aws cli code
import subprocess

def menu():
	print("\n-----------aws commands executor-------")

	def command_executor(command):
		x = subprocess.getstatusoutput(command)
		print(x[1])
		if x[0] == 0 :
			print("command executed successfully")


	# menu_aws() will execute will display the menu and get the choice from user and prepare a command to be executed
	def menu_aws():
		while True:
			print(60*"-")
			print("\t1. Create a key pair")
			print("\t2. Create a new aws instance")
			print("\t3. Start a aws instance")
			print("\t4. Describe ec2 instance")
			print("\t5. Create a EBS volume")
			print("\t6. Attach a EBS volume to ec2 instance")
			print("\t7. Create s3 bucket")
			print("\t8. Upload a file in bucket")
			print("\t9. Create a distribution in aws CloudFront")
			print("\t10. Exit")
			print(60*"-")
			
			choice = int(input("Enter Choice : "))
			if choice == 1 :
				key_name = input("Enter key name : ")
				#original cli command for creating aws key-pair: aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem
				#but we want that user should give the name of key pair hence using string manipulation
				command = "aws ec2 create-key-pair --key-name " + key_name + " --output text > "+ key_name+".pem"
				print("Note: If the key-pair downloaded is not working for ssh login then remove the additional text[metadata of key-pair] from keypair_name.pem file.")
				command_executor(command)

			elif choice == 2:
				imageId = "ami-052c08d70def0ac62"
				instancetype = "t2.micro"
				instance_count = "1"
				key_name = input("key-name : ")
				print("Note : Default values are set so that you do not use options other than free tier")
				print("imageId = " + imageId + "\nInstance type = " + instancetype + "\nInstance count = " + instance_count)
				command = "aws ec2 run-instances --image-id "+ imageId + " --instance-type " + instancetype + " --count " + instance_count + " --key-name " + key_name
				command_executor(command)

			elif choice == 3:
				instanceId = input("Enter instance id to start a instance : ")
				command = "aws ec2 start-instances --instance-ids "+ instanceId 
				command_executor(command)

			elif choice == 4:
				command = "aws ec2 describe-instances" 
				command_executor(command)

			
			elif choice == 5:
				print("Note: Size is restricted to 5 Gib per volume to keep you bounded in free tier")
				size = input("Enter size of ebs volume : ")
				region = input("Enter availability zone : ")
				if int(size) <= 5 : 
					command = "aws ec2 create-volume --volume-type gp2 --size " + size + " --availability-zone " + region
				else: 
					print("Size must be less than 5 Gib")
				command_executor(command)
			
			elif choice == 6:
				volume_id = input("Enter Volume id of ebs storage : ")
				instance_id = input("Enter Instance id :")
				device = input("Enter device name[ex - /dev/sdf] : ")

				command = "aws ec2 attach-volume --volume-id " + volume_id + " --instance-id " + instance_id + " --device " + device
				command_executor(command)
			
			elif choice == 7:
				bucket_name = input("Enter bucket name : ")
				regions3 = input("Enter region : ")
				command = "aws s3api create-bucket --bucket " + bucket_name + " --region " + regions3
				command_executor(command)

			elif choice == 8:
				file_path = input("Enter file path[ex - c:\\users\\d\\desktop\\image.jpg] : ")
				bucket_name1 = input("Enter bucket name")
				filename = input("What should be the file name of your file in s3 bucket? :  ")

				command = "aws s3 cp " + file_path + " s3://" + bucket_name1 + "/" + filename
				command_executor(command)
			
			elif choice == 9:
				domain_name = input("Enter a domain to create a distribution : ")
				command = "aws cloudfront create-distribution --origin-domain-name " + domain_name
				command_executor(command)
			

			elif choice == 10:
				print("Exited from AWS command Executer")
				break


	# check_requirements() is used to check whether aws cli is installed in the system on which the menu driven program is going to run
	def check_requirements():
		print("checking requirements...")
		x = subprocess.getstatusoutput("aws --version")
		if x[0] != 0 :
			print("AWS cli not installed on your system")
			print("please install aws cli")
			ch = input("press [y/n] = " )
			if ch == "y" or ch == "Y":
				os.system(" curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip\"")
				os.system("unzip awscliv2.zip")
				os.system("sudo ./aws/install")
				check_requirements()
			else:
				print("aws cli required to run aws commands")
				
		else:
			print("aws cli is installed on system..")
			print("Everything is okay!!")
			print("Configuring aws cli..")
			os.system("aws configure")
			menu_aws()

	
	check_requirements()


#To test this program, call menu() or remove the comment from next line
#menu()

'''
	references:
	https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-keypairs.html


	use the command sudo pip install awscli --force-reinstall --upgrade if even after aws installation on linux system you are getting error that aws not found


'''
