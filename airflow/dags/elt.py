from airflow import DAG
from airflow.operators.bash_operator import BashOperator # type: ignore
from airflow.operators.python_operator import PythonOperator # type: ignore
from datetime import timedelta
from pyspark.sql import SparkSession

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": "2024-11-27 15:35:00",
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG("elt", default_args=default_args, schedule_interval="*/3 * * * *", max_active_runs=1)

push_file = BashOperator(
    task_id="push_file",
    bash_command="spark-submit /opt/airflow/spark/push_file_airflow.py",
    dag=dag
)

transform_data = BashOperator(
    task_id="transform_data",
    bash_command="source /opt/airflow/source/env.sh && spark-submit /opt/airflow/spark/transform_data_airflow.py",
    dag=dag
)

push_file >> transform_data
