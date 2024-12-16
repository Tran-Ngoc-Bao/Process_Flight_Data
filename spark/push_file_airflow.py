from pyspark.sql import SparkSession
from sys import argv

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Push file").getOrCreate()

    time_df = spark.read.option("header", "true").csv("hdfs://namenode:9000/time")
    time = time_df.first()
    year = int(time["year"])
    month = int(time["month"])

    if (year == 2022 and month >= 8) or year > 2022:
        pass
    else:
        df = spark.read.option("header", "true").csv("/opt/airflow/source/flight_data/raw/Flights_" + str(year) + "_" + str(month) + ".csv")
        df.write.mode("overwrite").parquet("hdfs://namenode:9000/staging/" + str(year) + "/" + str(month))
        