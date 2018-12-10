# Synthetic data generator

Application that generates synthetic data for BigData concept proofs. Provides relational (postgres), nonrelational (mongodb) and streaming data with Kafka. The infra is built based on containers.
### Architecture
![Architecture](https://github.com/DataGenPoc/synthetic-data-generator/blob/master/docs/architecture.jpg?raw=true)


### Structure of the project
      - data-generator : Contains the script responsible for generating synthetic data        
      - data-publisher : Contains the script responsible for generating the data stream
      - docker-compose.yml : Orchestration of the application
 

#### Environment
In the data-generator and data-publisher containers, you need to identify the local IP of your host machine and the Kafka port.

    - KAFKA_HOST: <kafka_advertised_host_name>:<kafka_advertised_port>
 
In the Kafka configuration, it is necessary to inform the local ip of your host machine.

    - KAFKA_ADVERTISED_HOST_NAME: <your-local-ip>

General variables: Must be defined in an ".env" file at the project root

    KAFKA_HOST=<kafka_advertised_host_name>:<kafka_advertised_port>
    KAFKA_ADVERTISED_HOST_NAME=<your-local-ip>
    KAFKA_ADVERTISED_PORT=9092
    KAFKA_AUTO_CREATE_TOPICS_ENABLE=true
    KAFKA_CREATE_TOPICS=messages:1:1
    KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
    MONGO_INITDB_ROOT_USERNAME=foo
    MONGO_INITDB_ROOT_PASSWORD=foo
    POSTGRES_PASSWORD=foo
    POSTGRES_USER=foo
    QUANTIY_RECORDS=10
    QUANTIY_RECORDS_NOISE_PERCENT=30
    PROVIDER = <PROVIDER_NAME>
    KAFKA_RETENTION_MS=86400000
    POSTGRES_DB_NAME=foo
    MONGO_DB_NAME=foo
 
#### 
```sh
cd synthetic-data-generator
docker-compose up -d --build
```
   
#### Run with docker compose
```sh
cd synthetic-data-generator
docker-compose up -d --build
```

#### Ports
```sh
    - 5432 => Postgres
    - 5433 => Postgres admin
    - 27017 => MongoDB
    - 9092 => Kafka
```

#### Topics
```sh
    BASECOMPRASPDV_DDL
    BASECONSUMIDOR_BOT_DDL
    SELLOUT_TB_LOJA_VENDA_SO_DDL
```
