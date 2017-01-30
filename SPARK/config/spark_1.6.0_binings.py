import os
import sys
import glob

os.environ['SPARK_HOME']='/opt/cloudera/parcels/CDH-5.8.3-1.cdh5.8.3.p0.2/lib/spark'

os.environ['HADOOP_CONF_DIR']='/etc/hadoop/conf/'

SPARK_HOME = os.getenv('SPARK_HOME', None)

if SPARK_HOME:
    os.environ['PATH'] = "%s:%s/bin" % (os.getenv("PATH", ""), SPARK_HOME)
else:
    print("SPARK_HOME needs to be set (eg. export SPARK_HOME=/opt/spark)")
    sys.exit(4)

# Workaround to assembly jar not providing pyspark on Yarn and PythonPath not being passed through normally
#
# so this is actually to generate SPARK_YARN_USER_ENV which allows the pyspark to execute across the cluster

sys.path.insert(0, os.path.join(SPARK_HOME, 'python'))
for lib in glob.glob(os.path.join(SPARK_HOME, 'python/lib/py4j-*-src.zip')):
    sys.path.insert(0, lib)
#
# simply appending causes an Array error in Java due to the first element
# being empty if SPARK_YARN_USER_ENV isn't already set
if os.getenv('SPARK_YARN_USER_ENV', None):
    os.environ['SPARK_YARN_USER_ENV'] = os.environ['SPARK_YARN_USER_ENV'] + ",PYTHONPATH=" + ":".join(sys.path)
else:
    os.environ['SPARK_YARN_USER_ENV'] = "PYTHONPATH=" + ":".join(sys.path)
