# Start Spark Thrift server on temp table

Start a spark-shell: `spark-shell --conf spark.sql.hive.thriftServer.singleSession=true`

```
import org.apache.spark.sql.hive.thriftserver._
import org.apache.spark.sql.hive.HiveContext

val hiveContext = new HiveContext(sc)

val myDF = spark.read(...)

myDF.createOrReplaceTempView("testtable")
hiveContext.setConf("hive.server2.thrift.port","10015")
HiveThriftServer2.startWithContext(hiveContext)

```

Connect: `beeline -u jdbc:hive2://<hostname>:10015/default`
