# 3.Write a simple program in SCALA using Apache Spark framework

// Simple Apache Spark Program in Scala

import org.apache.spark.sql.SparkSession

object SimpleSparkProgram {
  def main(args: Array[String]): Unit = {

    // Create Spark Session
    val spark = SparkSession.builder()
      .appName("Simple Spark Program")
      .master("local[*]")
      .getOrCreate()

    // Create sample data
    val data = Seq(1, 2, 3, 4, 5)

    // Convert data into RDD
    val rdd = spark.sparkContext.parallelize(data)

    // Perform transformation (square each number)
    val squaredRDD = rdd.map(x => x * x)

    // Display output
    println("Squared Numbers:")
    squaredRDD.collect().foreach(println)

    // Stop Spark Session
    spark.stop()
  }
}