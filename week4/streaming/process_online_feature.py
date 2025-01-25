import json
import boto3
import base64
import json

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    for record in event['Records']:
       #Kinesis data is base64 encoded so decode here
       payload=base64.b64decode(record["kinesis"]["data"])
       my_json = payload.decode('utf8')
       print(my_json)
       json_object = json.loads(my_json)
       print(json_object["children"])
       dynamodb.put_item(TableName='customer', Item={'id':{'S': str(json_object["id"])},'children':{'N': str(json_object["children"])}})
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
  
