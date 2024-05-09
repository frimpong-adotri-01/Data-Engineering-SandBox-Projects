# Setup docker training exercism env


<image src="./images/Exercism+docker.png" width=1000 center>

[<img src="https://img.shields.io/badge/Docker-20.10.22-blue.svg?logo=docker   ">](https://docker.com/)
[<img src="https://img.shields.io/badge/Exercism--CLI-3.3.0--linux--x86_64-blueviolet.svg?logo=exercism   ">](https://github.com/exercism/cli/releases)

---
---
## 1. Objectif(s)
Ce projet vise à mettre en place un environnement de développement automatiquement configuré pour traiter des exercices Exercism en local. Le container hébergeant cet environnement se base sur une image Ubuntu:rolling.

---
---
## 2. Fonctionnement
Le fonctionnement est le suivant:
- On défini un `Dockerfile` qui créera le workspace Exercism et copiera les fichiers nécessaire à la mise en place de la configuration Exercism.

- Ensuite, le fichier `setup.sh` sera appelé pour configurer l'environnement d'exercism. Il installera des utilitaires annexes notamment ceux permettant une connexion SSH au container. Par ailleurs il exécutera des commandes qui téléchargeront Exercism-CLI et configurera partiellement l'environnement Exercism. Pour finir il ingérera une configuration permettant de colorer syntaxiquement l'environnement.

---
---
## 3. Exécution

Se positionner dans le répertoire `Data-Engineering-SandBox-Projects`. 
On commence par builder l'image à partir du Dockerfile. Cela se fait en exécutant la commande suivante (remplacer la variable "image_name" par le nom donné à votre image buildée):
```bash
docker build -t image_name .
```
<image src="./images/build.png" width=1000>

Puis on créé le container qui va héberger notre environnement de développement avec la commande (remplacer la variable "container_name" par le nom donné à votre container et la variable "image_name" par le nom donné à votre image buildée):
```bash
docker run -d -p local_port:22 --name container_name image_name
```
<image src="./images/run.png" width=1000>

Connectez vous au terminal bash de votre container
- Soit en ligne de commande (remplacer la variable "container_name" par le nom donné à votre container):
```bash
docker exec -it container_name bash
```
- Soit via VSCode (en installant préalablement l'extension "Docker" afin d'accéder au container directement depuis VSCode)

Ensuite, exécuter la commande ci-dessous pour enrégistrer votre jeton Exercism dans une variable d'environnement:
```bash
export EXERCISM_TOKEN=your_exercism_token
```

Enfin, exécuter la commande ci-dessous pour configurer l'environnement d'exercism:
```bash
exercism configure --token=$EXERCISM_TOKEN --workspace="/home/dev/exercism"
```
<image src="./images/exec.png" width=1000>

L'environnement est complètement configuré et on peut commencer à travailler.

QUELQUES COMMANDES EXERCISM PRATIQUES

```bash
exercism help  # Pour obtenir de l'aide sur les commandes Exercism
exercism submit  # Pour soumettre un exercice Exercism (en étant positionné dans le répertoire de l'exercice à soumettre)
exercism download --track=langage --exercise=nom_de_l_exercice  # Pour telecharger un exercice Exercism
```
<image src="./images/e-help.png" width=1000>

<image src="./images/e-dload.png" width=1000>

<br/>

<br />

## **CRÉDITS**

**AUTEUR :** ADOTRI Frimpong
