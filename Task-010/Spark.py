from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark import SparkConf

if __name__ == '__main__':
	sc = SparkContext("local", "Counting these words for you")
	tokenized = sc.textFile("/home/field/Desktop/Shakespeare.txt").flatMap(lambda line: line.split(" "))
	wordcounting = tokenized.map(lambda word: (word, 1)).reduceByKey(lambda v1,v2:v1 +v2)
	LIIS = wordcounting.collect()
	print (LIIS)
	LIIS1 = sc.parallelize(LIIS)

	#LOCAL DUMP ::::::

	#LIIS1.saveAsTextFile("/home/field/Desktop/RESULT")

	#HDFS DUMP ::::::

	#LIIS1.saveAsTextFile("hdfs://Master:9000/Spark")
	


SparkContext.stop()
