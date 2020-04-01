from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("X").getOrCreate()

jd = spark.read.json(r"D:\dev\large_dataset\simple_json.json")
jd.show(4)
jd.schema
