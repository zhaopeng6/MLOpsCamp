import boto3
from locust import events
import time


runtime= boto3.client('runtime.sagemaker')

endpoint_name = "test-sagemaker"


def make_sagemaker_request_load_test(client, payload):
    custom_attributes = "c000b4f9-df62-4c85-a0bf-7c525f9104a4"
    content_type = "text/csv"                                        # The MIME type of the input data in the request body.
    accept = "*/*"                                              # The desired MIME type of the inference in the response.
    start_at = time.time()
    print(payload)
    try:
        response = runtime.invoke_endpoint(EndpointName=endpoint_name,
                                           ContentType='text/csv',
                                           Body=payload)
        print(response)
        # status = response['ResponseMetadata']['HTTPStatusCode']
        # if status == 200:
        #     events.request_success.fire(
        #         request_type='Talk to endpoint',
        #         name=endpoint_name,
        #         response_time=int((time.time() - start_at) * 1000),
        #         response_length=0,
        #     )
        # response_body = response['Body']
        # response_str = response_body.read().decode('utf-8')
        # response_dict = eval(response_str)
        # print(len(response_dict['scores']))
    except Exception as e:
        print(e)
        events.request_failure.fire(
            request_type='Failed to talk to endpoint',
            name=endpoint_name,
            response_time=int((time.time() - start_at) * 1000),
            response_length=0,
            exception=e,
        )
