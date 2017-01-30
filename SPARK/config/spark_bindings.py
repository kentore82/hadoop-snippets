# -*- coding: utf-8 -*-

# Spark bindings for Jupyter Notebooks 
# Author: Ken Tore Tallakstad, ken.tore@sherpaconsulting.no
# Date: 04.12.2016

import getpass
import os

os.environ["JAVA_HOME"] = "/usr/java/jdk1.8.0_60"

def init(version='1.6.0',df_api=True,master='local[2]',dri_mem=2,num_exec=2,exec_mem=1,exec_cores=1,app_name=getpass.getuser()+' sparkapp'):
	jupyter_conf_path='/share/hadoop_custom/conf/spark/'	

	if version=='1.6.0':
		execfile(jupyter_conf_path+"spark_1.6.0_binings.py")
		from pyspark import SparkConf
		from pyspark import SparkContext
		
		sconf=custom_spark_conf(SparkConf(),version,master,num_exec,exec_mem,dri_mem,exec_cores,app_name)
		sc = SparkContext(conf=sconf)
	
	elif version=='2.0.2':
		execfile(jupyter_conf_path+"spark_2.0.2_binings.py")
		from pyspark import SparkConf
		from pyspark import SparkContext
		
		sconf=custom_spark_conf(SparkConf(),version,master,num_exec,exec_mem,dri_mem,exec_cores,app_name)
		sconf.set('spark.driver.maxResultSize',exec_mem)
		
		sc = SparkContext(conf=sconf)
			
	else:
		print("Spark version must be either '1.6.0' or '2.0.2'!")
		exit(1)

	if df_api==True:
		# Import Spark DataFrame API's
		from pyspark import HiveContext
		sqlContext = HiveContext(sc)
		import pyspark.sql.types as T
		import pyspark.sql.functions as F
		from pyspark.sql.window import Window
		from pyspark.sql import Row
	
		return sc,sqlContext,T,F,Window,Row

	else:
		return sc

def custom_spark_conf(sconf,version,master,num_exec,exec_mem,dri_mem,exec_cores,app_name):
	if int(version.split('.')[0])>=2 and master[0:5]!='local':
		master_yarn=master.split('-')[0]
		dmode=master.split('-')[1]
		sconf.set('spark.submit.deployMode',dmode)
		sconf.set('spark.master',master_yarn)
	else:
		sconf.set('spark.master',master)
	
	sconf.set('spark.executor.instances',str(num_exec))#Number of executors
	#sconf.set('spark.shuffle.service.enabled',True)
	#sconf.set('spark.dynamicAllocation.enabled',True)
	sconf.set('spark.executor.memory',str(exec_mem)+'g')
	sconf.set('spark.driver.memory',str(dri_mem)+'g')
	sconf.set('spark.executor.cores',str(exec_cores)) # number of cores on same worker
	sconf.set('spark.app.name',app_name) #Application Name
	sconf.set('spark.app.id',app_name)

	return sconf


