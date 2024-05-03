from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
from tasks.velib_data_to_mongodb_TASKS import get_velib_api_data, load_to_mongo


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
