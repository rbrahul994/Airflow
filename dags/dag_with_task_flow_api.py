import datetime
from airflow.decorators import dag, task


default_args = {
    "owner": "rahul",
    "retries": 5,
    "retry_delay": datetime.timedelta(minutes=2)
}


@dag(
	dag_id="python_decorator_dag_v2",
    description="Python operator DAG",
    default_args=default_args,
    start_date= datetime.datetime(2023, 9, 22),
    schedule_interval="@daily"
)
def hello_world_etl():

	@task(multiple_outputs=True)
	def get_name():
		return {
			"f_name": "rahul",
			"l_name": "B"
		}

	@task()
	def get_lang():
		return "python"

	@task()
	def greet(f_name, l_name, lang):
		print(f"Hellow wolrd: My name is {f_name} {l_name} "
			f"and I love {lang}!"
			)

	name_dict = get_name()
	lang = get_lang()
	greet(f_name=name_dict["f_name"], l_name=name_dict["l_name"], lang=lang)


greet_dag = hello_world_etl()