from airflow.sdk import dag, task
import pendulum

@dag(
    dag_id = "first_schedule_dag",
    start_date = pendulum.datetime(2026, 5, 5, tz="Asia/Ho_Chi_Minh"),
    schedule = "@daily",
    is_paused_upon_creation = False,
    catchup = True
)

def first_schedule_dag():
    
    @task.python
    def first_task():
        print("Hello World")

    @task.python
    def second_task():
        print("Hello world from hello world")

    @task.python
    def third_task():
        print("Hello world from hello world from hello world. DAG completed!")
    
    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

# Instantiating the DAGs
first_schedule_dag()