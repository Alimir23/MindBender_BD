import scala.io.Source
import scala.collection.immutable.ListMap
import java.io.PrintWriter
import java.io._


lazy val initial = io.Source.fromFile("/home/field/Desktop/temptxt.txt").getLines.mkString

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

// def printToFile(f: java.io.File)(op: java.io.PrintWriter => Unit){
// 	val p = new java.io.PrintWriter(f)
// 	try { op(p) } finally { p.close() }
// }

def main(args: Array[String]){

	var counted_stuff = countwords(args)
	val ordered_map = order_map(counted_stuff)
	printing(ordered_map)

	new PrintWriter("Scala_Output_Final.txt") {
		ordered_map.foreach {
			case (k, v) =>
				write(k + ":" + v)
				write("\n")
		}
	}
}

main(Shakee)

// libraryDependencies ++= Seq(
//   "org.apache.hadoop" % "hadoop-client" % "2.7.0"
// )

// import org.apache.hadoop.conf.Configuration
// import org.apache.hadoop.fs.{FileSystem, Path}
 
// object Hdfs extends App {
 
//   def write(uri: String, filePath: String, data: Array[Byte]) = {
//     System.setProperty("HADOOP_USER_NAME", "Mariusz")
//     val path = new Path(filePath)
//     val conf = new Configuration()
//     conf.set("fs.defaultFS", uri)
//     val fs = FileSystem.get(conf)
//     val os = fs.create(path)
//     os.write(data)
//     fs.close()
//   }
// }

