from airflow.sdk import dag, task
from pendulum import datetime, duration
from airflow.timetables.trigger import DeltaTriggerTimetable

@dag(
    dag_id = "delta_scheduling",
    start_date = datetime(2026, 5, 5, tz="Asia/Ho_Chi_Minh"),
    schedule = DeltaTriggerTimetable(duration(days = 3)), # or DeltaTriggerTimetable(days = 3)
    end_date = datetime(2026, 5, 6, tz="Asia/Ho_Chi_Minh"), 
    is_paused_upon_creation = False,
    catchup = True
)

def delta_scheduling():
    
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
delta_scheduling()