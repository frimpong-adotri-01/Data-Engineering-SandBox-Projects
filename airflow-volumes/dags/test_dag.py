from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def test_task():
    print("Hello World!")

with DAG(
            dag_id="Test-dag",
            description="Airflow DAG for Data-Engineering-SandBox-Projects",
            schedule_interval="@daily",
            start_date=datetime(2022, 1, 1),
            catchup=False) as dag:
    
    test_task:PythonOperator = PythonOperator(task_id="test_task", python_callable=test_task)
