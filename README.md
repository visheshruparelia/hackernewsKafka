Language: Python

Library Dependencies: haxor, kafka-python, flask, elasticsearch

Installing dependencies:
1. cd into the root directory of the project.
2. Run “pip3 install -r requirements.txt”

Install Docker:
https://docs.docker.com/v17.12/install/linux/docker-ce/ubuntu/#install-using-the-repository


Install Docker-compose:
https://docs.docker.com/compose/install/

Steps to run:
Kafka, Zookeeper, ElasticSearch, Kibana:
2. cd into root directory of the project
3. Run “sudo docker-compose up --no-recreate”

Producer: 
1. cd into the root directory of the project
2. Run “python3 producer.py”

Local Consumer:
1. cd into local_consumer folder
2. Run “python3 consumer.py”

Remote Consumer:
1. cd into flask_app folder
2. Run “python3 consumerflask.py”

Elastic Search Consumer:
1. cd into elastic_consmer folder
2. Run “python3 consumer.py”
