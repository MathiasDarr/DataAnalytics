package basics

import org.apache.spark.{SparkConf, SparkContext}

object WordCount {

  def getSparkContext() = {

    val conf = new SparkConf().
      setMaster("local").
      setAppName("LearnScalaSpark")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    sc
  }


  def main(args: Array[String]): Unit = {

//    val conf = new SparkConf().
//      setMaster("local").
//      setAppName("LearnScalaSpark")
//    val sc = new SparkContext(conf)
    val sc = getSparkContext()

    sc.setLogLevel("ERROR")

    val helloWorldString = "Hello World!"
    print(helloWorldString)
  }
}
