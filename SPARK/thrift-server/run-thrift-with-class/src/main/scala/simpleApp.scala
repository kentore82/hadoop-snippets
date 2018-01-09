// simple Scala app to submit with spark-submit / spark-thrift
package simpleSpark

import scala.math.random
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql._

object simpleApp extends App {
  val spark = SparkSession
      .builder
      .appName("Spark DataFrame")
      .getOrCreate().enableHiveSupport()

  val testDF = Seq((52.1,11.3),(39.3,11.2),(44.3,22.4)).toDF("lat","lon")

  testDF.createOrReplaceTempView("test")
  
  testDF.show()
    
  spark.stop()
  
  

}
