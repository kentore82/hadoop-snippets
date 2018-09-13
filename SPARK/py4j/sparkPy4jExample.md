# An example using `com.databricks.spark.avro.SchemaConverters`

There does not seem to be a python binding for using databricks avro schema to Spark StructType converter. However it is possible to use this class through py4j.

## Import the ususal stuff
```python
import spark_bindings

from pyspark.sql import SparkSession
from pyspark import SparkConf

sconf = SparkConf()

sconf.set('spark.submit.deployMode','client')
sconf.set('spark.master','yarn')

app_name="I am Spark"
sconf.set('spark.app.name',app_name)

spark = ( SparkSession
    .builder
    .config(conf=sconf)
    .enableHiveSupport()
    .getOrCreate()
)
```

## Verify that using py4j through spark session works. 

```python
java_list = spark._jvm.java.util.ArrayList()
java_list.append(214)
java_list.append(21433)
java_list.append(2)
spark._jvm.java.util.Collections.sort(java_list)
java_list
```




    [2, 214, 21433]



## Avro schema example from SVV api
```python
from avro.schema import parse

my_avro_schema_string = """
{
 "name": "Vaerutsatt_veg",
 "type": "record",
 "fields": [
  {
   "name": "type",
   "type": [
    "null",
    "string"
   ],
   "default": null
  },
  {
   "name": "vegobjekt",
   "type": [
    "null",
    {
     "type": "record",
     "name": "vegobjekt",
     "fields": [
      {
       "name": "id",
       "type": [
        "null",
        "int"
       ],
       "default": null
      },
       .
       .
       .
       .

"""
```

## Verify if my_avro_schema_string is valid avro 
```
my_avro_schema = schema = parse(my_avro_schema_string)
```

## Parse avro schema string to a org.apache.Schema object
```python
java_avro_schema=spark._jvm.org.apache.avro.Schema.parse(my_avro_schema_string)
```

## Convert to spark struct type

```
spark_struct_type=spark._jvm.com.databricks.spark.avro.SchemaConverters.toSqlType(java_avro_schema)
```
> Note that the org.databricks.spark.avro package is not on the classpath by default. Import with `--packages com.databricks:spark-avro_2.11:4.0.0` 


## Success!

```python
spark_struct_type.toString()

   u'SchemaType(StructType(StructField(type,StringType,true), StructField(vegobjekt,StructType(StructField(id,IntegerType,true),....

```
> Note, spark_struct_type is a Java object, must be serialized to corresponding pyspark datatypes

```python

spark.stop()
```
