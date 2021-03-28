def namenode():
	import os
	print("\t\t\tProvide the details about namenode:")
	namenode_IP = input("\t\t\tProvide IP at which you want to configure namenode:")
	namenode_folder = input("\t\t\tProvide the Folder name for Namenode:")
	os.system("rm -rf {}".format(namenode_folder))#firstly removing if created 
	os.system("mkdir {}".format(namenode_folder))#creating folder
	namenode_port = input("\t\t\tProvide Port Number at which you want to run namenode service:")
	
	file_hdfs_nn = open("/etc/hadoop/hdfs-site.xml","w")#opening the hdfs file to configure 
	#hdfs data
	
	hdfs_data_nn =  '''<?xml version="1.0"?>                                            
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(namenode_folder)
	file_hdfs_nn.write(hdfs_data_nn) #writing in data

	file_core_nn = open("/etc/hadoop/core-site.xml", "w")
	
	#core file data
	core_data_nn = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_IP,namenode_port)
	file_core_nn.write(core_data_nn)   
namenode()