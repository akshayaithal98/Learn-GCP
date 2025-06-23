from google.cloud import storage
import os
import pandas as pd
from dotenv import load_dotenv
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""
#os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

load_dotenv()

def upload_to_bucket(bucket_name,blob_path,file_name):
    try:
        storage_client=storage.Client()
        bucket=storage_client.bucket(bucket_name)
        blob=bucket.blob(blob_path)
        blob.upload_from_filename(file_name)
        print(f"File: {file_name} uploaded in path {bucket_name}/{blob_path}")

    except Exception as e:
        print(e)

def load_from_bucket(bucket_name,blob_path):
    try:
        storage_client=storage.Client()
        bucket=storage_client.bucket(bucket_name)
        blob=bucket.blob(blob_path)
        with blob.open("r") as file:
            df=pd.read_csv(file)
        return df
    
    except Exception as e:
        print(e)

if __name__=="__main__":
    df=pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
    file_name="sample_file.csv"
    df.to_csv(file_name,index=False)
    bucket_name="sumne_bucket"
    blob_path=file_name
    upload_to_bucket(bucket_name,blob_path,file_name)
    
    df_retrieved=load_from_bucket(bucket_name,blob_path)
    print(df_retrieved.head())
