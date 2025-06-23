from google.cloud import pubsub_v1
import json
from secret_manager import GCP_PROJECT_ID
from dotenv import load_dotenv

load_dotenv()


def publish_message_to_topic():
    client=pubsub_v1.PublisherClient()
    topic=client.topic_path(GCP_PROJECT_ID,"my_topic")
    data=json.dumps({"Person":"akshay","age":20})
    byte_string_data=data.encode('UTF-8')
    future=client.publish(topic,byte_string_data)
    print(future.result())


publish_message_to_topic()




