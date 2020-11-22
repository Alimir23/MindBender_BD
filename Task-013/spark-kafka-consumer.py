from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

if __name__ == '__main__':

	def process(rdd):
		if not rdd.isEmpty():
			global ss
			df = ss.createDataFrame(rdd, schema=["id", "text"])
			df.show()
			df.write.saveAsTable(name="tweets",format="hive", mode="append")



	sc = SparkContext(appName="Kafka_to_spark")
	ssc= StreamingContext(sc, 10)
	ss = SparkSession.builder.appName("Kafka_to_spark").config("spark.sql.warehouse.dir","/user/hive/warehouse").config("hive.metastore.uris","thrift://localhost:9083").enableHiveSupport().getOrCreate()
	

	ks = KafkaUtils.createDirectStream(ssc, 
		['colab_tweets'], {'metadata.broker.list': 'localhost:9099'})

	lines = ks.map(lambda x: json.loads(x[1]))


	filtered = lines.filter(lambda x: x.get("lang") == "en").map(lambda x: (x.get("id"), x.get("text")))

	filtered.foreachRDD(process)


	ssc.start()
	ssc.awaitTermination()
