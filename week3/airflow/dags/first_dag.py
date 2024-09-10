from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta

default_args = {
    'owner':'student',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id = 'first_dag',
    default_args = default_args,
    description = 'example dag',
    start_date = datetime(2024,7,23),
    schedule_interval = '@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = "echo hello world, this is 1st task"
    )
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = "echo hello world, this is 2nd task"
    )
    task1.set_downstream(task2)