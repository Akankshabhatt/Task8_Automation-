def client():
	import os
	namenode_IP = input("\t\t\tProvide namenode IP: ")
	namenode_port = input("\t\t\tProvide port number of namenode: ")
	print(''' \t\t\t Select Option:
		Option1: Do you Want Change replication factor and block size both
		Option2: Do you Want to Change only replication_factor
		Option3: Do you Want to Change only block size
		Option4: Don't Want to do anything.
	''')
	
	option = int(input("\t\t\tSelect Any of these options:"))

	if(option==1):
		replication_size=int(input("Enter replication_factor:"))
		block_size=int(input("Enter block size in bytes:"))
		file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
		hdfs_data_cn =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.replication</name>
<value>{}</value>
</property>

<property>
<name>dfs.block.size</name>
<value>{}</value>
</property>
</configuration>\n'''.format(replica_size,block_size)
		file_hdfs_cn.write(hdfs_data_cn)

	if(option==2):
		replication_factor=int(input("Enter replication_factor:"))
		file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
		hdfs_data_cn =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.replication</name>
<value>{}</value>
</property>
</configuration>\n\n'''.format(replication_factor)
		file_hdfs_cn.write(hdfs_data_cn)

	if(option==3):
		block_size=int(input("Enter block size in bytes:"))
		file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
		hdfs_data_cn =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.block.size</name>
<value>{}</value>
</property>
</configuration>\n'''.format(block_size)
		file_hdfs_cn.write(hdfs_data_cn)

	if(option==4):
		file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
		hdfs_data_cn =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
</configuration>\n'''
		file_hdfs_cn.write(hdfs_data_cn)


	file_core_cn = open("/etc/hadoop/core-site.xml", "w")
	core_data_cn = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_IP,namenode_port)
	file_core_cn.write(core_data_cn)   
client()