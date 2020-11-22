from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

if __name__ == '__main__':

	def process(rdd):
		if not rdd.isEmpty():
			global ss
			df = ss.createDataFrame(rdd, schema=["state"])
			df.show()
			#print(str(rdd.collect()))



	sc = SparkContext(appName="CovidTracker")
	ssc= StreamingContext(sc, 10)
	ss = SparkSession.builder.appName("CovidTracker").getOrCreate()
	#ss.SparkContext.setLogLevel("WARN")

	ks = KafkaUtils.createDirectStream(ssc, 
		['covidapi'], {'metadata.broker.list': 'localhost:9099'})

	lines = ks.flatMap(lambda x: json.loads(x[1]))


	filtered = lines.map(lambda x: x.get("state"))
	

	#filtered = lines.map(lambda x: (x.get("state"), x.get("date"), x.get("positiveIncrease"), x.get("positive"), x.get("probableCases"), x.get("pending")))

	filtered.foreachRDD(process)
	#lines.foreachRDD(process)


	ssc.start()
	ssc.awaitTermination()
