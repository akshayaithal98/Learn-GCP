# """
# create table `eloquent-theme.python_dataset.sample`
# (name String,age int64)
# partition by  RANGE_BUCKET(age, GENERATE_ARRAY(0, 100, 10));
# """

from google.cloud import bigquery
import pandas as pd
import os

os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
GCP_PROJECT_ID="eloquent-theme"
DATASET="python_dataset"



def load_df_to_bqtable(df):
    table_name="sample"
    table=f"{GCP_PROJECT_ID}.{DATASET}.{table_name}"
    client=bigquery.Client()
    job=client.load_table_from_dataframe(df,table)    
    job.result()
    print("df uploaded")

def read_table(query):
    client=bigquery.Client()
    results=client.query(query)
    results_list = [tuple(row.values()) for row in results]

    return results_list


if __name__=="__main__":
    df=pd.DataFrame({"name":["a","b","c"],"age":[20,30,40]})

    load_df_to_bqtable(df)
    query=f"select * from {DATASET}.sample"
    result=read_table(query)
    print(result)



    

