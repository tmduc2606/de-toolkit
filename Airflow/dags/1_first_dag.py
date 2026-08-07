from airflow.sdk import dag, task

@dag(
    dag_id = "first_dag",
)

def first_dag():
    
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
first_dag()