

**Language** : Python
**Library Dependencies** : haxor, kafka-python, flask, elasticsearch

## **Installing dependencies:**

 1. cd into the root directory of the project.
 2. Run &quot;pip3 install -r requirements.txt&quot;
 3.  **Install Docker:** [Docker docs](https://docs.docker.com/v17.12/install/linux/docker-ce/ubuntu/#install-using-the-repository)
 4.  **Install Docker Compose:** [Docker-Compose docs](*https://docs.docker.com/compose/install/)


## **Steps to run:**

**1. Kafka, Zookeeper, ElasticSearch, Kibana:**
  - cd into root directory of the project
  - Run &quot;sudo docker-compose up --no-recreate&quot;

  **Outcomes:**

- Kafka will run on port 9092
- Zookeeper will run on port 2181
- ElasticSearch will run on port 9200
- Kibana will run on port 5601


**2. Producer:** 
- cd into the root directory of the project
 - Run &quot;python3 producer.py&quot;


**Outcome:** The script will keep publishing data to a topic named &quot;story&quot; in the kafka bus.


**3. Local Consumer:**
  - cd into local\_consumer folder
  - Run &quot;python3 consumer.py&quot;


**Outcome:** The script will pull the data from the bus and append it to consumerdata.csv


**4. Remote Consumer:**
  - cd into flask\_app folder
  - Run &quot;python3 consumerflask.py&quot;


**Outcome:** Webpage will be hosted on [http://localhost:5000](http://localhost:5000/)

**5.  Elastic Search Consumer:**
  - cd into elastic\_consmer folder
  - Run &quot;python3 consumer.py&quot;


**Outcome:** Data will be indexed to ElasticSearch under index &quot;hn\_story&quot; and can be viewed from Kibana console at [http://localhost:5601](http://localhost:5601/)

