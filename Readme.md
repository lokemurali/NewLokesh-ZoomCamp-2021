
## Docker commands used :
###################################################################################
#currently working and connected with DBewere and Python:
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -v $(pwd)/data:/var/lib/postgresql/data -d postgres
docker stop some-postgres
docker stat some-postgres
"if the port is being used already - in mac terminal
sudo lsof -i : 5432<portnumber>
sudo kill 9 <PID>"


######Working Image for postgresdb with nwetwork:
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -v $(pwd)/data:/var/lib/postgresql/data -d postgres
######Working Image for postgresdb with nwetwork:
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -v $(pwd)/data:/var/lib/postgresql/data --network=pg-network -d postgres

## PGADMIN Image for Docker:
Intreactive Mode:
docker run -it \
    -p 80:80 \
    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' \
    -d dpage/pgadmin4

#with network:
docker run -it \
    -p 80:80 \
    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' \
    --network=pg-network \
    --name pgadmin-doc \
    -d dpage/pgadmin4

## Calling Ingest_data.py file using cli by passing command line parameteres
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

## Running Python by passing the parameters in the Command line interface:
python Ingest_data.py --user=postgres --password=mysecretpassword --host=localhost --port=5432 --db=postgres --table_name=new_taxi_yellow --url=${URL}
## Building Docker for Ingest to run on the container:
    >Docker build -t taxi_ingest:v001 .
    ## this creates a container for our ingest code:
    ## Now we can run the docker image by passing all the python code parameters
    ## we are running this docker image on the same network which we run the postgres image and pgadmin before.
Docker run -it \
    --network=pg-network \
     taxi_ingest:v001 \
      --user=postgres \
      --password=mysecretpassword \
      --host=localhost \
      --port=5432 \
      --db=postgres \
      --table_name=new_taxi_yellow \
      --url=${URL}
    
(base) m0l0ge6@m-ycfpkx9v6v zoomcamp-2023 % Docker run -it \
    --network=pg-network \
     ingest_data:v001 \
      --user=postgres \
      --password=mysecretpassword \
      --host=172.19.0.2 \
      --port=5432 \
      --db=postgres \
      --table_name=new_taxi_yellow \
      --url=${URL}   


Sample for postgres docker image createion with volume mapping:
docker pull dpage/pgadmin4
docker run -p 443:443 \
    -v /private/var/lib/pgadmin:/var/lib/pgadmin \
    -v /path/to/certificate.cert:/certs/server.cert \
    -v /path/to/certificate.key:/certs/server.key \
    -v /tmp/servers.json:/pgadmin4/servers.json \
    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' \
    -e 'PGADMIN_ENABLE_TLS=True' \
    -d dpage/pgadmin4

## NEW CHANGES test

# After running the Docker compose, I ran the docker for python to load the data into postgres using the network docker compose created and the host name as Postgres service name in the docker compose.
(base) m0l0ge6@m-ycfpkx9v6v ~ % docker network ls
NETWORK ID     NAME                    DRIVER    SCOPE
d7a1ee177eb1   bridge                  bridge    local
4e6128bbade4   host                    host      local
f897d5e62abe   none                    null      local
09720f476502   pg-network              bridge    local
27ba9dfe2430   zoomcamp-2023_default   bridge    local
(base) m0l0ge6@m-ycfpkx9v6v ~ % cd documents

 Docker run -it \
    --network=zoomcamp-2023_default \
     ingest_data:v001 \
      --user=postgres \
      --password=mysecretpassword \
      --host=PostgresDatabase \
      --port=5432 \
      --db=postgres \
      --table_name=new_taxi_yellow \
      --url=${URL}   

