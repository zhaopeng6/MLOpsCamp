import time

from locust import between, task, TaskSet
import csv
from locust.contrib.fasthttp import FastHttpUser
import sys
from locust import events
import boto3


endpoint_name = "mwaa-sm-endpoint-8c9a554702024efdbb647defc6717bb0"
runtime = boto3.client('runtime.sagemaker')
csv.field_size_limit(sys.maxsize)


class SageMakerUser(FastHttpUser):
    abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.results = []
        self.count = 0
        with open('data.csv', newline='') as csvfile:
            name_reader = csv.reader(csvfile, delimiter='\n', quotechar='|')
            for row in name_reader:
                self.results.append(row)


class SageMakerTasks(TaskSet):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        index = self.user.count % len(self.user.results)
        # make_sagemaker_request_load_test(self.user.client, self.user.results[index])
        # make_sagemaker_request_load_test(self.user.client, self.user.results[index][0])
        self.user.count += 1
        start_at = time.time()
        try:
            response = runtime.invoke_endpoint(EndpointName=endpoint_name,
                                               ContentType='text/csv',
                                               # need to write our string into CSV format
                                               Body=self.user.results[index][0])
            # print(response)
            status = response['ResponseMetadata']['HTTPStatusCode']
            if status == 200:
                events.request_success.fire(
                    request_type='Talk to endpoint',
                    name=endpoint_name,
                    response_time=int((time.time() - start_at) * 1000),
                    response_length=0,
                )
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


class ModelUser(SageMakerUser):
    tasks = [SageMakerTasks]

