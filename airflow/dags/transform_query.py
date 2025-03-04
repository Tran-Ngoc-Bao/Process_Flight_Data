from airflow import DAG
from airflow.operators.bash_operator import BashOperator # type: ignore
from airflow.operators.python_operator import PythonOperator # type: ignore
from datetime import timedelta
from pyspark.sql import SparkSession
import os

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": "2025-01-05 05:00:00",
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG("transform_query", default_args=default_args, schedule_interval="*/5 * * * *", max_active_runs=1)

year = 2030
month = 1

spark = SparkSession.builder.appName("Get time from HDFS").getOrCreate()
df = spark.read.option("header", "true").csv("hdfs://namenode:9000/time")
time = df.first()
year = int(time["year"])
month = int(time["month"])

def increase_time_def():
    global year
    global month

    if year == 2030:
        pass
    else:
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        
        columns = ["year", "month"]
        data = [(year, month)]
        df = spark.createDataFrame(data, columns)
        df.write.option("header", "true").mode("overwrite").csv("hdfs://namenode:9000/time")

def query_data_def():
    global year
    global month

    if (year == 2022 and month >= 8) or year > 2022:
        pass
    else:
        string = ''
        with open('/opt/airflow/sql/template/month.sql', 'r') as f:
            string = f.read()

        string_replace = string.replace('{year}', str(year)).replace('{month}', str(month))
        with open(f'/opt/airflow/sql/month/month_{year}_{month}.sql', 'w') as f:
            f.write(string_replace)

        os.system(f'cd /opt/airflow/source && ./trino --server http://coordinator:8080 --file /opt/airflow/sql/month/month_{year}_{month}.sql')

        if month % 3 == 0:
            string = ''
            with open('/opt/airflow/sql/template/quarter.sql', 'r') as f:
                string = f.read()

            quarter = int(month / 3)
            string_replace = string.replace('{year}', str(year)).replace('{quarter}', str(quarter))
            with open(f'/opt/airflow/sql/quarter/quarter_{year}_{quarter}.sql', 'w') as f:
                f.write(string_replace)
            
            os.system(f'cd /opt/airflow/source && ./trino --server http://coordinator:8080 --file /opt/airflow/sql/quarter/quarter_{year}_{quarter}.sql')

            if month % 12 == 0:
                string = ''
                with open('/opt/airflow/sql/template/year.sql', 'r') as f:
                    string = f.read()

                string_replace = string.replace('{year}', str(year))
                with open(f'/opt/airflow/sql/year/year_{year}.sql', 'w') as f:
                    f.write(string_replace)
                
                os.system(f'cd /opt/airflow/source && ./trino --server http://coordinator:8080 --file /opt/airflow/sql/year/year_{year}.sql')

transform_data = BashOperator(
    task_id="transform_data",
    bash_command=f"source /opt/airflow/source/env.sh && spark-submit /opt/airflow/spark/transform_data_airflow.py {year} {month}",
    dag=dag
)

query_data = PythonOperator(
    task_id="query_data",
    python_callable=query_data_def,
    dag=dag
)

increase_time = PythonOperator(
    task_id="increase_time",
    python_callable=increase_time_def,
    dag=dag
)

transform_data >> query_data >> increase_time
