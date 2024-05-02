from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
import requests
from pymongo import MongoClient
from pathlib import Path
from dotenv import load_dotenv
import os


def get_velib_api_data():
    data = requests.get(
        url="https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=20"
    ).json()["results"]

    return data


def load_to_mongo(data):
    retrieved_data = data.xcom_pull(task_ids=["get_velib_api_data"])
    path_to_dotenv_file = Path("./.env")
    load_dotenv(path_to_dotenv_file)

    client = MongoClient(
        host="127.0.0.1",
        port=27017,
        username=os.getenv("MONGO_INITDB_ROOT_USERNAME"),
        password=os.getenv("MONGO_INITDB_ROOT_PASSWORD"),
        authMechanism="SCRAM-SHA-256",  # SCRAM-SHA-256 is supported by MongoDB 4.0 or later (We're using Mongo 5.0.26 in the docker-compose.yaml file)
    )
    velib_db = client.velib_db
    velib_collection = velib_db[f"velib_data__{datetime.now().strftime('%Y%m%d')}__"]
    velib_collection.insert_many(retrieved_data)


with DAG(
    dag_id="Velib-data-to-MongoDB",
    description="Airflow DAG for ETL-with-Velib-API",
    schedule_interval="@hourly",
    start_date=datetime.now(),
    catchup=False,
) as dag:

    get_velib_api_data: PythonOperator = PythonOperator(
        task_id="get_velib_api_data", python_callable=get_velib_api_data
    )

    load_to_mongo: BranchPythonOperator = BranchPythonOperator(
        task_id="load_to_mongo", python_callable=load_to_mongo
    )

    # Connection of differents Airflow tasks
    get_velib_api_data >> load_to_mongo
