from airflow.sdk import dag, task

@dag(
    dag_id = "versioned_dag",
)

def versioned_dag():
    
    @task.python
    def first_task():
        print("Hello World")

    @task.python
    def second_task():
        print("Hello world from hello world")

    @task.python
    def third_task():
        print("Hello world from hello world from hello world. DAG completed!")

    @task.python
    def versioned_task():
        print("Hello the extreme world!")
    
    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    versioned = versioned_task()

    first >> second >> third >> versioned

# Instantiating the DAGs
versioned_dag()