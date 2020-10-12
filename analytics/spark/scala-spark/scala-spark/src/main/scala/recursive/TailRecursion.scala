package recursive

object TailRecursion {
  def gcd(a: Int, b: Int): Int =
    if(b==0) a
    else
      gcd(b, a %b)

  def main(args: Array[String]): Unit ={
    println("The gcd of 12 & 18 is " + gcd(12, 18))
  }
}
