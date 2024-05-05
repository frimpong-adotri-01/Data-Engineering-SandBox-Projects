# Airflow-ETL-with-Velib-API

<image src="./images/ETL-Airflow-Velib.png" width=1000 center>

[<img src="https://img.shields.io/badge/Docker-20.10.22-blue.svg?logo=docker   ">](https://hub.docker.com/r/grafana/grafana/tags)
[<img src="https://img.shields.io/badge/docker--compose-v2.15.1-blue.svg?logo=docker   ">](https://hub.docker.com/r/grafana/grafana/tags)
[<img src="https://img.shields.io/badge/Apache/airflow-2.7.1-ff69b4.svg?logo=apacheairflow   ">](https://hub.docker.com/r/grafana/grafana/tags)
[<img src="https://img.shields.io/badge/Mongo-5.0.26-successgreen.svg?logo=mongodb   ">](https://hub.docker.com/r/grafana/grafana/tags)
[<img src="https://img.shields.io/badge/Postgres-13-blue.svg?logo=postgresql   ">](https://hub.docker.com/r/grafana/grafana/tags)
[<img src="https://img.shields.io/badge/Python-3.11.7-yellow.svg?logo=python   ">](https://hub.docker.com/r/grafana/grafana/tags)

---
---
## 1. Objectif(s)
Ce projet vise à mettre en place une architecture basée sur des containers Docker. Au sein de cette architecture, on retrouve principalement des containers:
- **Airflow** : pour l'orchestration de l'execution des taches
- **Postgres** : pour la base de données des metadata de Airflow
- **MongoDB** : pour la base de données où on stocke les informations des velibs
- **MongoDB-express** : pour l'interface graphique de MongoDB

<br/>

---
---
## 2. Fonctionnement
Le fonctionnement est le suivant:
On dispose d'une API Vélib qui met à disposition des données via un point de terminaison et de 2 bases de données: PostgreSQL et MongoDB. On dispose aussi de 2 tâches Airflow associées à un DAG (Workflow). L'une récupère les données de l'API Vélib et l'autre les sauvegarde dans la base de données MongoDB. Parallèlement, on garde une trace de chaque exécution du workflow Airflow en sauvegardant les metadata dans la base de données Postgres.

<br/>

---
---
## 3. Exécution

Il faut préalablement avoir installé les outils suivants:
- **Docker**: version 20.10.22
- **Docker-compose**: version v2.15.1
- **Python**: version 3.11.7

Ensuite, se placer dans le répertoire `Data-Engineering-SandBox-Projects` et créer un fichier intitulé `.env` qui contiendra toutes les variables d'environnement (particulièrement les credentials) passées dans le fichier docker-compose.yaml.

```bash
touch .env
```

 Copier-coller le snippet ci-dessous dans le fichier `.env` en remplaçant les variables 'xxxxx' par les valeurs de votre choix :

```ini
AIRFLOW_UID=501
AIRFLOW_IMAGE_NAME=apache/airflow:2.7.1
AIRFLOW_PROJ_DIR=./airflow-volumes
# AIRFLOW WEBSERVER CREDENTIALS
_AIRFLOW_WWW_USER_USERNAME=xxxxx
_AIRFLOW_WWW_USER_PASSWORD=xxxxx
# POSTGRE DATABASE CREDENTIALS
POSTGRES_USER=xxxxx
POSTGRES_PASSWORD=xxxxx
# MONGODB DATABASE CREDENTIALS
MONGO_INITDB_ROOT_USERNAME=xxxxx
MONGO_INITDB_ROOT_PASSWORD=xxxxx
# MONGO-EXPRESS GUI CREDENTIALS
MONGOEXPRESS_ADMIN_USERNAME=xxxxx
MONGOEXPRESS_ADMIN_PASSWORD=xxxxx
```

Ensuite exécuter les commandes suivantes séquentiellement :

- Pour l'initialisation des composantes Airlow dans la stack Docker-compose :
```bash
docker compose up airflow-init
```
<image src="./images/airflow-init.png" width=1000>

<br/>

- Pour lancer toute la stack Docker-compose :
```bash
docker compose up -d
```
<image src="./images/docker-compose.png" width=1000>

<br/>

- Vérifier le status des containers et s'assurer que toute la stack aie un status **"healthy"**:

<image src="./images/docker-ps.png" width=1000>

<br/>

- On se rend sur le webserver Airflow pour tester le DAG qu'on a défini dans le fichier `airflow-volumes/dags/velib_data_to_mongodb_DAG.py` :

<image src="./images/airflow-webserver.gif" width=1000>

<br/>

- On se connecte à la base de données MongoDB pour afficher les informations des vélibs récoltés :

<image src="./images/mongo.gif" width=1000>

<br/>

- On se connecte à la base de données PostgreSQL pour observer les metadata des DAGs Airflow :

<image src="./images/postgres.gif" width=1000>

<br/>

- Pour stopper toute la stack Docker-compose :
```bash
docker compose down
```
<image src="./images/dockercompose-down.png" width=1000>

<br/>

<br />

## **CRÉDITS**

**AUTEUR :** ADOTRI Frimpong

