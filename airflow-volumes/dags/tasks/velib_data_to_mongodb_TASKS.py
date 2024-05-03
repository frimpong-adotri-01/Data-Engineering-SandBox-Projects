from airflow.models import TaskInstance
from typing import List
import requests
from pymongo import MongoClient
import os
from datetime import datetime


def get_velib_api_data() -> List[dict]:
    """
    Retrieves data from the Velib API.

    Returns:
        List[Dict]: A list of dictionaries containing the retrieved data from the Velib API.
    """
    # Make a GET request to the Velib API
    response = requests.get(
        url="https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=20"
    )

    # Parse the response as JSON and return the "results" key
    return response.json()["results"]


def load_to_mongo(ti: TaskInstance) -> None:
    """
    Loads retrieved data from a task into a MongoDB collection.

    Args:
        ti (TaskInstance): The TaskInstance object representing the current task.

    Returns:
        None

    Raises:
        None

    Side Effects:
        - Connects to the MongoDB server using the provided credentials.
        - Inserts the retrieved data into the 'velib_data' collection in the 'velib_db' database.
        - The collection name is dynamically generated based on the current date.

    Example:
        load_to_mongo(ti)
    """
    retrieved_data = ti.xcom_pull(task_ids=["get_velib_api_data"])  # type: List[Dict]
    print(retrieved_data[0])

    client = MongoClient(
        host=f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@mongo:27017/"
    )
    velib_db = client.velib_db  # type: Database
    velib_collection = velib_db[f"velib_data__{datetime.now().strftime('%Y%m%d')}__"]  # type: Collection
    velib_collection.insert_many(retrieved_data[0])
    velib_collection = velib_db[f"velib_data__{datetime.now().strftime('%Y%m%d')}__"]
    velib_collection.insert_many(retrieved_data[0])