from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration example") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING) USING hive")