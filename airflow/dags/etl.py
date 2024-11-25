
from airflow import DAG
from airflow.operators.bash_operator import BashOperator # type: ignore
from airflow.operators.python_operator import PythonOperator # type: ignore
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 11, 25, 11, 0, 0),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG("etl", default_args=default_args, schedule_interval="*/3 * * * *")

year = 2018
month = 1

def increase_time_def():
    global year
    global month

    if month == 12:
        year += 1
        month = 1
    else:
        month += 1

push_file = BashOperator(
    task_id="push_file",
    bash_command=f"spark-submit /opt/airflow/spark/push_file_airflow.py {year} {month}",
    dag=dag
)

transform_data = BashOperator(
    task_id="transform_data",
    bash_command=f"source /opt/airflow/source/env.sh && spark-submit /opt/airflow/spark/transform_data_airflow.py {year} {month}",
    dag=dag
)

increase_time = PythonOperator(
    task_id="increase_time",
    python_callable=increase_time_def,
    dag=dag
)

push_file >> transform_data >> increase_time