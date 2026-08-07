from airflow.sdk import dag, task
import pendulum
from airflow.timetables.trigger import CronTriggerTimetable

# Cron syntax for 4pm daily: "0 16 * * *"
# Format: minute hour day_of_month month day_of_week 
@dag(
    dag_id = "cron_scheduling",
    start_date = pendulum.datetime(2026, 5, 5, tz="Asia/Ho_Chi_Minh"),
    schedule = CronTriggerTimetable("0 16 * * MON-FRI", timezone = "Asia/Ho_Chi_Minh"),
    end_date = pendulum.datetime(2026, 5, 6, tz="Asia/Ho_Chi_Minh"),
    is_paused_upon_creation = False,
    catchup = True
)

def cron_scheduling():
    
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
cron_scheduling()