#for pubsub push we need to have a public endpoint url, it will send api request for that url, no need to call any client.
#u can receive msg in params

from google.cloud import pubsub_v1
from dotenv import load_dotenv
from secret_manager import GCP_PROJECT_ID
import time
load_dotenv()

def pull_messages_from_topic():
    client=pubsub_v1.SubscriberClient()
    subscription=client.subscription_path(GCP_PROJECT_ID,"python_pull_sub")

    def callback(message):
        print(f"Received message:{message.data.decode('UTF-8')} ")
        message.ack()  #Acknowledge the message so it is not re-delivered,or else when pulling again, the delivered msg will be redelviered

    client.subscribe(subscription,callback=callback)
    while True:
        time.sleep(10)


if __name__=="__main__":
    pull_messages_from_topic()

