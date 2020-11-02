import scala.io.Source
import scala.collection.immutable.ListMap


val initial = io.Source.fromFile("/home/field/Desktop/Shakespeare.txt").getLines.mkString

//Shakee.foreach(print)
//println(Shakee.getClass)

val removepunct = initial.replaceAll(""".[\p{Punct}&&[^.]].""", "").toLowerCase()
//Shakee.foreach(print)

val Shakee = removepunct.split(" ").map(_.trim)

//Shakee.foreach(println)

def countwords (dat : Array[String]) : Map[String, Int] = {
 	dat.toSet.map((word: String) => (word, dat.count(_ == word))).toMap

}
def order_map(dat: Map[String, Int]): Map[String, Int] = {
	return ListMap(dat.toSeq.sortWith(_._2 < _._2):_*)
}

def printing(dat: Map[String, Int]) = {
	for ((k,v) <- dat) printf("%s : %s\n", k , v)
}

def main(args: Array[String]){

	var counted_stuff = countwords(args)
	val ordered_map = order_map(counted_stuff)
	printing(ordered_map)
}

main(Shakee)
// print(countwords(Shakee))