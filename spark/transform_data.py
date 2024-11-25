from pyspark.sql import SparkSession

def solution():
    global year
    global month

    df = spark.read.parquet("hdfs://namenode:9000/staging/" + str(year) + "/" + str(month))
    df.repartition(1).write.mode("overwrite").parquet()

    if month == 12:
        year += 1

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Insert Data Warehouse").getOrCreate()

    year = 2018
    month = 1

    flag = True
    while flag:
        try:
            solution()
        except:
            print("Don't worry about this error", year, month)
            flag = False
    # solution()

    # Select columns not too much null
    # Process duplicated rows
    # Process date data
    # Cast data type
    # Insert data

    # Ingest data to staging
    # Code transform data
    # Processed data storage
    # Demo Trino
    # Demo Superset
    # Demo Spark ML ???