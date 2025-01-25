import datetime
import json
import random
import boto3

STREAM_NAME = "customerfeature"
AWS_REGION = "us-west-1"

def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'id': 5,
        'children': 10,  # online feature
        'payment': 2,  # offline feature, need aggregation
    }


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")


if __name__ == '__main__':
    kinesis_client = boto3.client("kinesis", region_name = AWS_REGION)
    generate(STREAM_NAME, boto3.client('kinesis'))
