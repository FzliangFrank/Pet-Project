@main def hello() = println("Hello, World!")


/* interactively  readline*/
import scala.io.StdIn.readLine

@main def helloInteractive() =
  println("Please enter your name:")
  val name = readLine() // val is immutable var is not mutable

  println("Hello, " + name + "!")