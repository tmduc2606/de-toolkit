from airflow.sdk import dag, task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
@dag
def dag_orchestrator_parent():

    trigger_first_dag = TriggerDagRunOperator(
        task_id = "trigger_first_orchestrator_dag",
        trigger_dag_id = "first_orchestrator_dag"
    )

    trigger_second_dag = TriggerDagRunOperator(
        task_id = "trigger_second_orchestrator_dag",
        trigger_dag_id = "second_orchestrator_dag"
    )

    trigger_first_dag >> trigger_second_dag

# Instantiating the DAG
dag_orchestrator_parent()