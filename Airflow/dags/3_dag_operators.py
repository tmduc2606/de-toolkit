from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator

@dag(
    dag_id = "operated_dag",
)

def dag_operators():
    
    @task.python
    def first_task():
        print("Hello World")

    @task.python
    def second_task():
        print("Hello world from hello world")
    
    @task.bash
    def bash_task_modern():
        return "echo https://airflow.apache.org/"
    
    bash_task_oldschool = BashOperator(
        task_id = "bash_task_oldschool",
        bash_command = "echo https://airflow.apache.org/",
    )
    
    # Defining task dependencies
    first = first_task()
    second = second_task()
    bash_modern = bash_task_modern()
    bash_oldschool = bash_task_oldschool

    first >> second >> bash_modern >> bash_oldschool

# Instantiating the DAGs
dag_operators()