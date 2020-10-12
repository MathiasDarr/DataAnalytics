package spark

import org.apache.spark.{SparkConf, SparkContext}

object HelloWorld {

  def main(args: Array[String]): Unit = {

    val conf = new SparkConf().
      setMaster("local").
      setAppName("LearnScalaSpark")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")

    val helloWorldString = "Hello World!"
    print(helloWorldString)

  }
}