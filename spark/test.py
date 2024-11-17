import pandas

if __name__ == "__main__":
    df = pandas.read_parquet("./airflow/source/flight_data/added_key/2018/1/1.parquet")
    print(df["id"][1])