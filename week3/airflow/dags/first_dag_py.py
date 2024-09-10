from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task
from datetime import datetime,timedelta

default_args = {
    'owner':'student',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

@dag(dag_id='first_dag_with_taskflow_api',
     default_args=default_args,
     start_date=datetime(2024,7,26),
     schedule_interval='@daily')
def hello_world_etl():
    @task()
    def get_name():
        return "jerry"
    
    @task()
    def get_age():
        return 19
    
    @task()
    def greet(name, age):
        print(f'Hello my name is {name}, '
              f'and my age is {age}')
        
    name = get_name()
    age = get_age()
    greet(name=name, age=age)

greet_dag = hello_world_etl()