@main def hello: Unit =
  println("Hello world!")
  println(msg)

def msg = "I was compiled by Scala 3. :)"

@main def goodbye: Unit = 
  println("Goodbye world")
  println(msg)