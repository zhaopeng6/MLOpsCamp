import boto3
import csv

test_endpoint = "mwaa-sm-endpoint-8c9a554702024efdbb647defc6717bb0"
runtime = boto3.client('runtime.sagemaker')

with open('data.csv', newline='') as csvfile:
    name_reader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in name_reader:
        response = runtime.invoke_endpoint(EndpointName=test_endpoint,
                                           ContentType='text/csv',
                                           # need to write our string into CSV format
                                           Body=row[0])
        response_body = response['Body']
        response_str = response_body.read().decode('utf-8')
        print(response_str) # prediction
        print(response['ResponseMetadata']['HTTPStatusCode']) # HTTP status code
        break
