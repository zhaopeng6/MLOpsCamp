import os
import io
import boto3
import json
import csv

ENDPOINT_NAME = "CustomerChurn"
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print(event)
    data = json.loads(json.dumps(event))
    print(data)
    payload = data['body']
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=str(payload))
    print(response)
    # more feature extractions for complicated cases
    result = json.loads(response['Body'].read().decode())
    
    cloudwatch = boto3.client('cloudwatch')
    response = cloudwatch.put_metric_data(
        MetricData = [{
                'MetricName': 'Result',
                'Dimensions': [
                    {
                        'Name': 'REGISTERED_SERVICE',
                        'Value': 'InferenceService'
                    },
                    {
                        'Name': 'APP_VERSION',
                        'Value': '1.0'
                    },
                ],
                'Unit': 'None',
                'Value': result
            }],
            Namespace='MLApp'
    )
    print(result)
    
    return result

# test json:
# {"body": "2.0,400.0,0.38571846040122537,2.0,4.177940384158745,0.0,3.745462710628048,250.0,3.699591756294294,1.0,11.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,0.0,0.0,1.0"}