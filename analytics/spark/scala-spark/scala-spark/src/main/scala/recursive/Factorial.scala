package recursive

object Factorial {
  def factorial(n: Int): Int =
    if (n==1) 1
    else factorial(n-1) * n

  def main(args: Array[String]): Unit = {
    println("THe factorial of 5 is " + factorial(5))

  }

}
