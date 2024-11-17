# IT3943 - Project 3 - SOICT - HUST

## Introduction
<ul>
  <li>Name of project: Build a Data Lake system to analyze flight data on Kaggle</li>
  <li>Project objective:
    <ul>
      <li>Process flight data on Kaggle with Data Lake system</li>
      <li>Use Spark SQL and Spark ML to analyze data</li>
    </ul>  
  </li>
</ul>

## Data flow
  <img src="https://github.com/Tran-Ngoc-Bao/Process_Flight_Data/blob/master/pictures/system.png">

## Deploy system
#### 1. Should pull and build images before
```sh
docker pull postgres bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8 bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8 bde2020/hadoop-resourcemanager:2.0.0-hadoop3.2.1-java8 bde2020/hadoop-nodemanager:2.0.0-hadoop3.2.1-java8 bde2020/hadoop-historyserver:2.0.0-hadoop3.2.1-java8
```
```sh
docker build ./airflow -t airflow
```
```sh
docker build ./superset -t superset
```

#### 2. Start system
```sh
docker compose up -d
```

#### 3. Set Trino on Airflow cluster
```sh
docker exec -u root -it airflow-webserver chmod +x /opt/airflow/source/trino; docker exec -u root -it airflow-scheduler chmod +x /opt/airflow/source/trino
```

#### 4. Start DAG on Airflow webserver

#### 5. Build enviroment Superset
```sh
./superset/bootstrap-superset.sh
```
  
#### 6. Visualize data on Superset with SQLalchemy uri
```
trino://hive@trino:8080/hive
```

## Demo

## Report
