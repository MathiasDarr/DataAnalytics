package functional

object Reductions{
  def main(args: Array[String]): Unit ={
    val a = Array(20, 12, 6, 15, 2, 9)
    val additionReduction = a.reduceLeft(_ + _)
    println("The reduction of these values w/ a + operator is " + additionReduction)
  }


}
