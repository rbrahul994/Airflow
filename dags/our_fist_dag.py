import datetime

# from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "rahul",
    "retries": 5,
    "retry_delay": datetime.timedelta(minutes=2)
}

with DAG(
        dag_id="fist_dag_v3",
        default_args=default_args,
        description="This is our first dag",
        start_date=datetime.datetime(2023, 9, 22),
        schedule_interval="@daily"
    ) as dag:
    task1 = BashOperator(
            task_id='first_task',
            bash_command="echo hello world, this is a new task."
        )

    task2 = BashOperator(
            task_id='second_task',
            bash_command="echo I will execute after dag 2."
        )

    task3 = BashOperator(
            task_id='Third_task',
            bash_command="echo I will also execute after task 1."
        )

    ### Task run method 1

    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    
    ### Task run method 2

    # task1 >> task2
    # task1 >> task3
    
    ### Task run method 3

    task1 >> [task2, task3]