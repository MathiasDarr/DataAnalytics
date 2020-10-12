package spark_basics

import org.apache.spark.{SparkConf, SparkContext}

object SparkBasics {
  def getSparkContext() = {

    val conf = new SparkConf().
      setMaster("local").
      setAppName("LearnScalaSpark")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    sc
  }


  def main(args: Array[String]): Unit = {
    val sc = getSparkContext()
    sc.setLogLevel("ERROR")

    val data = Array(6, 2, 3, 4, 5)
    val distData = sc.parallelize(data)

    val takeOne = distData.take(1)
    println(takeOne(0))
  }
}
