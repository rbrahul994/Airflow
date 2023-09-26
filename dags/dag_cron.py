import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "rahul",
    "retries": 5,
    "retry_delay": datetime.timedelta(minutes=2)
}

with DAG(
    dag_id="dag_cron_v1",
    default_args=default_args,
    description="This is our first dag",
    start_date=datetime.datetime(2023, 9, 20),
    schedule_interval="0 0 * * *"
    # @once  @houly       @daily     @weekly    @monthly   @yearly
    #        0 * * * *    0 0 * * *  0 0 * * 0  0 0 1 * *  0 0 1 1 *
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo this is an echo command"
    )