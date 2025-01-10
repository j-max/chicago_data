import pandas as pd
pd.set_option('display.max_columns', 500)
import psycopg2
from sqlalchemy import create_engine
import sqlalchemy as sqla

import sys
import os

base_dir = os.getcwd()
repo_name = "chicago_data"
root_path =base_dir.split(repo_name)[0] + repo_name 
sys.path.append(root_path)
from src.data_portal_api import get_portal_data

# connection establishment
conn = psycopg2.connect(
   database="chicago_schools",
    user='',
    password='',
    host='localhost',
    port= '5432'
)
 
conn.autocommit = True
 
# # Creating a cursor object
# cursor = conn.cursor()
 
# # query to create a database 
# sql = ''' CREATE database chicago_schools ''';
 
# # executing above query
# cursor.execute(sql)
# print("Database has been created successfully !!");
 
# # Closing the connection
# conn.close()


engine = create_engine('postgresql+psycopg2://[insert_username]:[insert_password]@localhost/chicago_schools')

progress_report_2324= 'https://data.cityofchicago.org/resource/2dn2-x66j.json'
pr_df = get_portal_data(progress_report_2324)

# these columns are dictionaries in the dowload, which mess up postgres
pr_df.drop(columns=["cps_school_profile", "website", "state_school_report_card"], inplace=True)
pr_df.to_sql('pr_2324', engine)

 