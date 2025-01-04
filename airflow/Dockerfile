FROM apache/airflow:2.6.1
USER root
RUN apt update
RUN apt install -y default-jdk 
USER airflow
RUN pip install pyspark confluent_kafka