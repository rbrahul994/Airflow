import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "rahul",
    "retries": 5,
    "retry_delay": datetime.timedelta(minutes=2)
}

with DAG(
    dag_id="catch_up_v1",
    default_args=default_args,
    description="This is our first dag",
    start_date=datetime.datetime(2023, 9, 20),
    schedule_interval="@daily",
    catchup=True    # run when to catup to current date # false when to try back fill
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo this is an echo command"
    )


# sudo docker exec -it 8d1844c4bcc3 bash
# airflow dags backfill -s 2023-09-20 -e 2023-09-26 catch_up_v1 #to back fill manully from the container
