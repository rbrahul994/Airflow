import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args ={
    "owner": 'rahul',
    "retries": 5,
    "retry_delay": datetime.timedelta(minutes=5)
}


def greet(text, ti):
    name = ti.xcom_pull(task_ids="get_details_task", key='name')
    second = ti.xcom_pull(task_ids="get_details_task", key='second')
    print(f"my name is {name} ", f"this is my {second} dag and ", f"{text}")
    return None

def get_name(ti):
    ti.xcom_push(key="name", value="rahul") 
    ti.xcom_push(key="second", value="python") 
    return None


with DAG(
        dag_id="python_op_dag",
        description="Python operator DAG",
        default_args=default_args,
        start_date= datetime.datetime(2023, 9, 22),
        schedule_interval="@daily"
    ) as dag:

    task1 = PythonOperator(
            task_id="greet",
            python_callable=greet,
            op_kwargs={"text": "I like python"}
        )
    task2 = PythonOperator(
            task_id="get_details_task",
            python_callable=get_name,
        )

    task2 >> task1
