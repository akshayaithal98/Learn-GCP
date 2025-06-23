#either you will be authenticated with service account attached with our instance only
#or else you can use GOOGLE_APPLICATION_CREDENTIALS to authenticate with our gcp account,
#client just searches for GOOGLE_APPLICATION_CREDENTIALS, 
#you can assign GOOGLE_APPLICATION_CREDENTIALS with a json file or encrpy and then assign it, anything is fine

import json
import base64
from google.oauth2 import service_account
from secret_manager import DATASET
from google.cloud import bigquery

#We can store this GOOGLE_CREDENTIALS_BASE64 in secret manager and load, 
#then we dont need to use json file since that is not as secure compared to this
with open("gcp_learning_service_account.json", "rb") as f:
    GOOGLE_CREDENTIALS_BASE64 = base64.b64encode(f.read()).decode()

#print(GOOGLE_CREDENTIALS_BASE64) 

decoded_credentials = base64.b64decode(GOOGLE_CREDENTIALS_BASE64).decode()
credentials_info = json.loads(decoded_credentials)
credentials = service_account.Credentials.from_service_account_info(credentials_info)

#verify the service account used 
from google.auth import default
def check_gcp_service_account():
    try:
        credentials, project = default()
        print(f"Active service account: {credentials.service_account_email}")
        print(f"Project ID: {project}")
    except Exception as e:
        print(f"Failed to retrieve service account: {str(e)}")

check_gcp_service_account()

#to test this credentials , we will query from bigquery 
def read_table(query):
    client=bigquery.Client(credentials=credentials)
    results=client.query(query)
    results_list = [tuple(row.values()) for row in results]

    return results_list

query=f"select * from {DATASET}.sample"
result=read_table(query)
print(result)