from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

if __name__ == "__main__":
    datawarehouse_location = 'hdfs://namenode:9000/processed_data'
    spark = SparkSession.builder.appName("Train data").config("spark.sql.warehouse.dir", datawarehouse_location).enableHiveSupport().getOrCreate()
        
    spark.sql("use processed_data")
    df = spark.sql("select Month, DayofMonth, DayOfWeek, DepTime, DepDelay from flight_2018")
    df = df.dropna()

    feature_columns = df.columns[:-1]
    assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
    data = assembler.transform(df)

    train, test = data.randomSplit([0.7, 0.3])
    algorithm = LinearRegression(featuresCol="features", labelCol="DepDelay")
    model = algorithm.fit(data)

    evaluation_summary = model.evaluate(test)

    prediction = model.transform(test)
    prediction.select(prediction.columns[4:])
