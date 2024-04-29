println("Hello, world")
val x = 1
x + x

var y = 0

println(s"hello calling ${x}")

if x != 0 then 
    println("not 0")
else if x == 0 then
    println("This is 0")
else 
  println("something else")

val name = "James"
val age = 30
println(s"$name is $age years old")


val height = 1.9d
f"$name%s is $height%2.2f meters tall"

var i = 2
val evenOrOdd = i match
  case 1 | 3 | 5 | 7 | 9 => println("odd")
  case 2 | 4 | 6 | 8 | 10 => println("even")
  case _ => println("some other number")


val list =
  for i <- 10 to 12
  yield i * 2

for
  i <- 1 to 10
  if i > 3
  if i < 6
  if i % 2 == 0
do
  println(i)
case class Person(name: String)

def speak(p: Person) = p match
  case Person(name) if name == "Fred" => println(s"$name says, Yubba dubba doo")
  case Person(name) if name == "Bam Bam" => println(s"$name says, Bam bam!")
  case _ => println("Watch the Flintstones!")

speak(Person("Fred"))      // "Fred says, Yubba dubba doo"
speak(Person("Bam Bam"))   // "Bam Bam says, Bam bam!"

val frank = Person("Frank")
