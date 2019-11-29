Language: Python
Library Dependencies: haxor, kafka-python, flask, elasticsearch
Installing dependencies:
cd into the root directory of the project.
Run “pip3 install -r requirements.txt”
Install Docker:
https://docs.docker.com/v17.12/install/linux/docker-ce/ubuntu/#install-using-the-repository


Install Docker-compose:
https://docs.docker.com/compose/install/

Steps to run:
Kafka, Zookeeper, ElasticSearch, Kibana:
cd into root directory of the project
Run “sudo docker-compose up --no-recreate”
Producer: 
cd into the root directory of the project
Run “python3 producer.py”
Local Consumer:
cd into local_consumer folder
Run “python3 consumer.py”
Remote Consumer:
cd into flask_app folder
Run “python3 consumerflask.py”
Elastic Search Consumer:
cd into elastic_consmer folder
Run “python3 consumer.py”
