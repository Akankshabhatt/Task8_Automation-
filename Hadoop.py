import os

def menu():
	print("\t\t\t---------------------------------")
	print("\t\t\t Hadoop Cluster Configuration ")
	print("\t\t\t---------------------------------")
	print(''' \t\t\tFOLLOW THE STEPS TO SETUP HADOOP CLUSTER:
		  \t\tStep:1 Provide the  details about Namenode.
		  \t\tStep:2 Provide the details about Datanode.
		  \t\tStep:3 Provide the details about Client.
	''')
	print("\n\t\t\tNote: You may need to enter the password multiple times.\n")

	NameNode_IP = input("\t\t\tProvide IP at which you want to configure the Namenode:")
	#copy namenode_setup.py into instance to execute 
	os.system("scp namenode_setup.py root@{}:/root/".format(NameNode_IP))
	#install python3 on the instance in case if not installed
	os.system("ssh root@{} yum install python3 -y".format(NameNode_IP))
	#setup namenode's core-site.xml and hdfs-site.xml
	os.system("ssh root@{} python3 namenode_setup.py".format(NameNode_IP))
	#format the namenode
	os.system("ssh root@{} hadoop namenode -format".format(NameNode_IP))
	#start the namenode
	os.system("ssh root@{} hadoop-daemon.sh start namenode".format(NameNode_IP))


	Datanode_IP = []
	counter_datanode = int(input("\t\t\tHow many datanode you want to configure: "))
	for i in range(0,counter_datanode):
		dip = input("\t\t\tProvide IP at which you want to configure the Datanode{}: ".format(i+1))
		Datanode_IP.append(dip)
		os.system("scp datanode_setup.py root@{}:/root/".format(Datanode_IP[i]))
		os.system("ssh root@{} yum install python3 -y".format(Datanode_IP[i]))
		os.system("ssh root@{} python3 datanode_setup.py".format(Datanode_IP[i]))#setup datanode's core-site.xml and hdfs-site.xml 
		os.system("ssh root@{} hadoop-daemon.sh start datanode".format(Datanode_IP[i]))	#start the datanode


	Client_IP = []
	counter_client = int(input("\t\t\tHow many client you want to configure: "))
	for i in range(0,counter_client):
		c_ip = input("\t\t\tGive IP at which you want to configure client:")
		Client_IP.append(c_ip)
		os.system("scp client_setup.py root@{}:/root/".format(Client_IP[i]))
		os.system("ssh root@{} yum install python3 -y".format(Client_IP[i]))

		os.system("ssh root@{} python3 client_setup.py".format(Client_IP[i]))#setup datanode core-site.xml and hdfs-site.xml
		
menu()