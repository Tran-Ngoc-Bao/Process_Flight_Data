from pyspark.sql import SparkSession
from hashlib import sha256

def check_leap_year():
    if year % 4:
        return False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return True

def increase_time():
    if month == 12 and day == 31:
        year += 1
        month = 1
        day = 1
    elif day == 31:
        month += 1
        day = 1
    elif month == 2 and (day == 29 or (check_leap_year() == False and day == 28)):
        month = 3
        day = 1
    elif day == 30 and month in [4, 6, 9, 11]:
        month += 1
        day = 1
    else:
        day += 1

def solution():
    df_ref = spark.read.parquet("hdfs://namenode:9000/staging/reference/" + str(year) + "/" + str(month) + "/" + str(day))
    # df_tran = spark.read.parquet("hdfs://namenode:9000/staging/transaction/" + str(year) + "/" + str(month) + "/" + str(day))


if __name__ == "__main__":
    datawarehouse_location = 'hdfs://namenode:9000/datawarehouse'
    spark = SparkSession.builder.appName("Create data warehouse").config("spark.sql.warehouse.dir", datawarehouse_location).enableHiveSupport().getOrCreate()
    spark.sql("use data_warehouse")
    
    year = 2018
    month = 1
    day = 1
    while True:
        try:
            solution()
        except:
            print("Don't worry about this error")