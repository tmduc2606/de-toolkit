from airflow.sdk import dag, task, asset, Asset
from pendulum import datetime
import os

# The upstream asset is declared here BY IDENTITY (name + uri must match
# asset_13.fetch_data exactly). DAG files stay self-contained: importing the
# producer module across files would register the same asset twice and trip
# AirflowDagDuplicatedIdException in the DagBag.
fetch_data = Asset(
    name = "fetch_data",
    uri = "/opt/airflow/logs/data/data_extract.txt",
)

@asset(
    schedule = fetch_data,
    # This is optional but good to include for clarity about the asset's 
    uri = "/opt/airflow/logs/data/data_processed.txt",
    name = "process_data"
)

def process_data(self):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(self.uri), exist_ok = True)

    # Simulate data fetching by writing to a file
    with open(self.uri, "w") as f:
        f.write(f"Data processed successfully")

    print(f"Data written to {self.uri}")
