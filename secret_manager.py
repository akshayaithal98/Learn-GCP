#https://cloud.google.com/secret-manager/docs/samples/

from google.cloud import secretmanager
import google_crc32c
import json
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gcp_learning_service_account.json"

def get_latest_secret_version(project_id,secret_id):
    client=secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response=client.access_secret_version(request={"name":name})

    # Verify payload checksum.
    crc32c = google_crc32c.Checksum()
    crc32c.update(response.payload.data)
    if response.payload.data_crc32c != int(crc32c.hexdigest(), 16):
        print("Data corruption detected.")
        return response

    payload = response.payload.data.decode("UTF-8")
    return payload


project_id="48***"
secret_id="python_projects_secrets"

payload=get_latest_secret_version(project_id,secret_id)

Variable=json.loads(payload)


DATASET=Variable.get("DATASET")
GCP_PROJECT_ID=Variable.get("GCP_PROJECT_ID")
print(DATASET,GCP_PROJECT_ID)


