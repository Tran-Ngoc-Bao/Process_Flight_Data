# IT3943 - Project 3 - SOICT - HUST

## Introduction
<ul>
  <li>Name of project: Build a Data Lake system to analyze flight data on Kaggle</li>
  <li>Project objective:
    <ul>
      <li>Process flight data on Kaggle with Data Lake system</li>
      <li>Use Spark Streaming and Spark SQL to process data</li>
      <li>Use Trino to query data and Superset to visualize data</li>
    </ul>  
  </li>
</ul>

## Data flow
  <img src="https://github.com/Tran-Ngoc-Bao/Process_Flight_Data/blob/master/pictures/system.png">

## Deploy system
#### 1. Should pull and build images before
```sh
docker pull confluentinc/cp-zookeeper confluentinc/cp-kafka provectuslabs/kafka-ui postgres bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8 bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8 bde2020/hadoop-resourcemanager:2.0.0-hadoop3.2.1-java8 bde2020/hadoop-nodemanager:2.0.0-hadoop3.2.1-java8 bde2020/hadoop-historyserver:2.0.0-hadoop3.2.1-java8 bde2020/hive:2.3.2-postgresql-metastore bde2020/hive-metastore-postgresql:2.3.0 trinodb/trino:457
```
```sh
docker build ./airflow -t airflow
```
```sh
docker build ./superset -t superset
```
```sh
docker build ./flask -t data-source
```

#### 2. Start system
```sh
docker-compose up -d
```

#### 3. Set Trino on Airflow cluster
```sh
docker exec -u root -it airflow-webserver chmod +x /opt/airflow/source/trino; docker exec -u root -it airflow-scheduler chmod +x /opt/airflow/source/trino
```

#### 4. Set Spark and Hadoop on Airflow cluster
```
Download Spark & Hadoop packages and Replace config in airflow/source
```
```
https://spark.apache.org/downloads.html
```
```
https://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz
```

#### 5. Download data source and Save raw as folder data_source to server backend
```
https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022/data?select=readme.md
```

#### 6. Build enviroment Superset
```sh
./superset/bootstrap-superset.sh
```
  
#### 7. Visualize data on Superset with SQLalchemy URI
```
trino://hive@coordinator:8080/hive
```

## Demo output
### Analysis of day of month
  <img src="https://github.com/Tran-Ngoc-Bao/Process_Flight_Data/blob/master/pictures/charts/phan-ph%E1%BB%91i-m%E1%BA%A1ng-l%C6%B0%E1%BB%9Bi-ti%E1%BA%BFp-th%E1%BB%8B-hang-khong-2024-11-30T14-42-52.691Z.jpg">

### Analysis of month of year
  <img src="https://github.com/Tran-Ngoc-Bao/Process_Flight_Data/blob/master/pictures/charts/d%E1%BB%99-tr%E1%BB%85-trung-binh-theo-hang-hang-khong-2024-11-30T15-13-50.328Z.jpg">

## Report
<ul>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Process_Flight_Data/blob/master/pictures/report/report.pdf">Report</a></li>
  <li><a href="https://github.com/Tran-Ngoc-Bao/Process_Flight_Data/blob/master/pictures/report/slide.pptx">Slide</a></li>
</ul>
