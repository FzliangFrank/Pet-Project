file://<HOME>/Dropbox/Personal/code/Pet%20Project/11-26%20Scala%20Kick%20Off/worksheet/src/main/scala/hello.worksheet.sc
### file%3A%2F%2F%2FUsers%2Ffrankliang%2FDropbox%2FPersonal%2Fcode%2FPet%2520Project%2F11-26%2520Scala%2520Kick%2520Off%2Fworksheet%2Fsrc%2Fmain%2Fscala%2Fhello.worksheet.sc:14: error: unclosed character literal
  println('seomthing')
                    ^

occurred in the presentation compiler.

action parameters:
uri: file://<HOME>/Dropbox/Personal/code/Pet%20Project/11-26%20Scala%20Kick%20Off/worksheet/src/main/scala/hello.worksheet.sc
text:
```scala
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
  println('seomthing')

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

```



#### Error stacktrace:

```
scala.meta.internal.tokenizers.Reporter.syntaxError(Reporter.scala:23)
	scala.meta.internal.tokenizers.Reporter.syntaxError$(Reporter.scala:23)
	scala.meta.internal.tokenizers.Reporter$$anon$1.syntaxError(Reporter.scala:33)
	scala.meta.internal.tokenizers.Reporter.syntaxError(Reporter.scala:25)
	scala.meta.internal.tokenizers.Reporter.syntaxError$(Reporter.scala:25)
	scala.meta.internal.tokenizers.Reporter$$anon$1.syntaxError(Reporter.scala:33)
	scala.meta.internal.tokenizers.LegacyScanner.fetchSingleQuote$1(LegacyScanner.scala:407)
	scala.meta.internal.tokenizers.LegacyScanner.fetchToken(LegacyScanner.scala:412)
	scala.meta.internal.tokenizers.LegacyScanner.nextToken(LegacyScanner.scala:211)
	scala.meta.internal.tokenizers.LegacyScanner.foreach(LegacyScanner.scala:1011)
	scala.meta.internal.tokenizers.ScalametaTokenizer.uncachedTokenize(ScalametaTokenizer.scala:24)
	scala.meta.internal.tokenizers.ScalametaTokenizer.$anonfun$tokenize$1(ScalametaTokenizer.scala:17)
	scala.collection.concurrent.TrieMap.getOrElseUpdate(TrieMap.scala:962)
	scala.meta.internal.tokenizers.ScalametaTokenizer.tokenize(ScalametaTokenizer.scala:17)
	scala.meta.internal.tokenizers.ScalametaTokenizer$$anon$2.apply(ScalametaTokenizer.scala:332)
	scala.meta.tokenizers.Api$XtensionTokenizeDialectInput.tokenize(Api.scala:25)
	scala.meta.tokenizers.Api$XtensionTokenizeInputLike.tokenize(Api.scala:14)
	scala.meta.internal.parsers.ScannerTokens$.apply(ScannerTokens.scala:914)
	scala.meta.internal.parsers.ScalametaParser.<init>(ScalametaParser.scala:33)
	scala.meta.parsers.Parse$$anon$1.apply(Parse.scala:35)
	scala.meta.parsers.Api$XtensionParseDialectInput.parse(Api.scala:25)
	scala.meta.internal.semanticdb.scalac.ParseOps$XtensionCompilationUnitSource.toSource(ParseOps.scala:17)
	scala.meta.internal.semanticdb.scalac.TextDocumentOps$XtensionCompilationUnitDocument.toTextDocument(TextDocumentOps.scala:206)
	scala.meta.internal.pc.SemanticdbTextDocumentProvider.textDocument(SemanticdbTextDocumentProvider.scala:54)
	scala.meta.internal.pc.ScalaPresentationCompiler.$anonfun$semanticdbTextDocument$1(ScalaPresentationCompiler.scala:374)
```
#### Short summary: 

file%3A%2F%2F%2FUsers%2Ffrankliang%2FDropbox%2FPersonal%2Fcode%2FPet%2520Project%2F11-26%2520Scala%2520Kick%2520Off%2Fworksheet%2Fsrc%2Fmain%2Fscala%2Fhello.worksheet.sc:14: error: unclosed character literal
  println('seomthing')
                    ^