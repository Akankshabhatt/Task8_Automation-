def datanode():
	import os
	datanode_folder = input("\t\t\tFolder name for datanode:")
	os.system("rm -rf {}".format(datanode_folder))
	os.system("mkdir {}".format(datanode_folder))
	namenode_IP = input("\t\t\tProvide namenode IP: ")
	namenode_port = input("\t\t\tProvide port number of namenode: ")
	file_hdfs_dn = open("/etc/hadoop/hdfs-site.xml","w")#opening hdfs-site.xml file
	 #data of hdfs of datanode
	hdfs_data_dn =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(datanode_folder)
	file_hdfs_dn.write(hdfs_data_dn) #writing the data

	file_core_dn = open("/etc/hadoop/core-site.xml", "w")#opening core-site.xml file
	core_data_dn = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_IP,namenode_port)
	file_core_dn.write(core_data_dn)   
datanode()
