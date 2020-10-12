package arrays

import scala.math.max
object Solution {
  def maxSubArray(nums: Array[Int]): Int = {
    def maxSum(x: List[Int], y:List[Int]):List[Int] = {
      //first element will save the max sum of elements from beginning
      //including current element
      val a = max(x(0) + y(0), y(0))
      //second element of list will contain the max sum of elements from
      //the beginning till current element (being optional)
      val b = max(x(1), a)
      List(a,b)
    }
    //convert each integer element into list of 2 with same value
    //first element will save the max sum of elements from beginning
    //including current element
    //second element of list will contain the max sum of elements from
    //the beginning till current element (being optional)
    val tmpNums = nums.map(c => List(c,c))
    tmpNums.reduceLeft(maxSum(_,_))(1)
  }

  def main(args: Array[String]): Unit ={
    println("HelloDd")
    var nums = Array(-2,1,-3,4,-1,2,1,-5,4)
    println("the first element of the array is "  + maxSubArray(nums))
  }

}
