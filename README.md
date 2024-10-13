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
#### 1. You should pull and build images in file docker-compose.yaml before

#### 2. Move to clone project and Start system
  
```sh
docker compose up -d
```

#### 3. Install java on airflow-webserver and airflow-scheduler

```sh
docker exec -u root -it [airflow-webserver/airflow-scheduler] bash
apt update && apt install default-jdk
```

#### 4. After start system, all port website of containers in <a href="https://github.com/Tran-Ngoc-Bao/Process_Flight_Data/blob/master/port.txt">here</a>

#### 5. Start DAG in Airflow cluster

#### 6. Move to folder superset and run

```sh
./superset/bootstrap-superset.sh
```
  
#### 7. Visualize data in Superset website

## Demo

## Report
