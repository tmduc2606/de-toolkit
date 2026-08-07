from airflow.sdk import dag, task

@dag(
    dag_id = "parallel_tasks",
)

def parallel_tasks():
    
    @task.python
    def extract_task(**kwargs):
        print("Extracting Data...")
        ti = kwargs["ti"]
        extracted_data_dict = {"api_extracted_data": [1, 2, 3],
                                "db_extracted_data": [4, 5, 6],
                                "s3_extracted_data": [7, 8, 9]}
        
        ti.xcom_push(key = "return_result", value = extracted_data_dict)

    @task.python
    def transform_task_api(**kwargs):
        ti = kwargs["ti"]
        api_extracted_data = ti.xcom_pull(task_ids = "extract_task", key = "return_result")["api_extracted_data"]

        print(f"Transforming API Data: {api_extracted_data}...")
        transformed_api_data = [i * 10 for i in api_extracted_data]

        ti.xcom_push(key = "return_result", value = transformed_api_data)

    @task.python
    def transform_task_db(**kwargs):
        ti = kwargs["ti"]
        db_extracted_data = ti.xcom_pull(task_ids = "extract_task", key = "return_result")["db_extracted_data"]

        print(f"Transforming API Data: {db_extracted_data}...")
        transformed_db_data = [i * 10 for i in db_extracted_data]

        ti.xcom_push(key = "return_result", value = transformed_db_data)
    
    @task.python
    def transform_task_s3(**kwargs):
        ti = kwargs["ti"]
        s3_extracted_data = ti.xcom_pull(task_ids = "extract_task", key = "return_result")["s3_extracted_data"]

        print(f"Transforming API Data: {s3_extracted_data}...")
        transformed_s3_data = [i * 10 for i in s3_extracted_data]

        ti.xcom_push(key = "return_result", value = transformed_s3_data)
    
    @task.bash
    def load_task(**kwargs):
        print("Loading data to destination")
        ti = kwargs["ti"]

        api_data = ti.xcom_pull(task_ids = "transform_task_api", key = "return_result")
        db_data = ti.xcom_pull(task_ids = "transform_task_db", key = "return_result")
        s3_data = ti.xcom_pull(task_ids = "transform_task_s3", key = "return_result")

        return f"echo 'Loaded Data: {api_data}, {db_data}, {s3_data}'"


    # Defining task dependencies
    extract = extract_task()
    api = transform_task_api()
    db = transform_task_db()
    s3 = transform_task_s3()
    load = load_task()

    extract >> [api, db, s3] >> load


# Instantiating the DAGs
parallel_tasks()

