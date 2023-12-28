
import pandas as pd
from time import time
import sqlalchemy 
import create_engine
from time import time
import argparse

def main(params):
    User = params.user
    Password = params.password
    Host=params.host
    Port=params.port
    DB=params.db
    Table_Name=params.table_name
    URL=params.url
    
  
#  User = "postgres"
#  Password = "mysecretpassword"
#  Host="localhost"
#  Port=5432
#  DB="postgres"
#  Table_Name="new_tax"
#  URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
    ##  Connecting Postgres Database:
    print(f"postgresql://{User}:{Password}@{Host}:{Port}/{DB}")
    engine = create_engine(f'postgresql://{User}:{Password}@{Host}:{Port}/{DB}')
    engine.connect()
    ## Download the Parquet file from the URL: 
    par_file_loc = URL
    df_par = pd.read_parquet(par_file_loc,engine="pyarrow")
    df_par.to_csv("/Users/m0l0ge6/Documents/ZoomCamp-2023/out.csv")
    df_par.head(0).to_sql(name=Table_Name,con=engine,if_exists = 'replace')
    st_time = time()
    df_par.to_sql(name=Table_Name,con=engine,if_exists = 'append')
    ed_time = time()
    print(f'total time taken {ed_time-st_time} ms')
if __name__ == '__main__':
# Parameters : #User,#Password,#Host,#Port#DBPage,#URL,#Table_Name
    parser = argparse.ArgumentParser(description='Ingest yello_taxi data to postgres')
    parser.add_argument('--user',help='Postgres Username')
    parser.add_argument('--password',help='Postgres Password')
    parser.add_argument('--host',help='Postgres Password')
    parser.add_argument('--port',help='Postgres Port')
    parser.add_argument('--db',help='Postgres DBname')
    parser.add_argument('--table_name',help='Postgres DB table name given in code')
    parser.add_argument('--url',help='URL for the YellowTaxi parquet file')
    args = parser.parse_args()
    main(args)
