## Chapter 0: Everyday Works of A Data Engineer
Abstract: Data Engineers build systems to collect, connect different sources, process data, automate the process, and deliver value through technical solutions. They create the foundation for all data work. Their expertise centers on building reliable pipelines, enabling all downstream data activities. Their roles includes
Designing data infrastructure and architecture
Creating and maintaining data pipelines
Ensuring data quality and availability
Before a data scientist even touches the data, a data engineering team has already built a pipeline that turns messy, raw inputs into something reliable and consistent. Think of it less as a one-time cleanup and more as a continuously running system.
At a high level, data engineers design automated pipelines (often called ETL or ELT as an abbrevation for Extract - Transform - Load) that handle data from ingestion to storage. The goal isn’t just cleaning once, but enforcing consistency every time new data arrives.
Ingestion with validation gates: Data flows in from APIs, databases, logs, or files. Right at this stage, engineers add validation rules (e.g., checking types, required fields, formats, and ranges). Tools like Apache Kafka or Apache NiFi are often used to stream and control incoming data. Bad records can be rejected, quarantined, or flagged immediately instead of polluting the system.
Schema enforcement and versioning: To keep things consistent, engineers define strict schemas (column names, data types, constraints). Systems like Apache Avro or Google BigQuery help enforce structure. If a data source suddenly changes format, the pipeline detects it instead of silently breaking downstream models.
Automated cleaning transformations: Cleaning rules are encoded into transformation steps
Standardizing formats (dates, currencies, text casing)
Handling missing values (impute, drop, or flag)
Deduplicating records
Normalizing inconsistent categories
These transformations run automatically in batch or streaming jobs using frameworks like Apache Spark or dbt.
Data quality checks (continuous testing): Engineers treat data like code getting tested. Tools like Great Expectations define expectations (e.g., “no nulls in user_id,” “values must be within range”). Pipelines fail or alert when expectations aren’t met, preventing bad data from propagating.
Centralized, curated storage layers: Cleaned data is stored in structured layers (often called bronze/silver/gold architecture)
Raw (unchanged data)
Cleaned (standardized, validated)
Curated (business-ready datasets)
Warehouses or lakes like Snowflake or Amazon Redshift ensure consistency and accessibility.
Orchestration and monitoring: All of this is scheduled and monitored using orchestration tools like Apache Airflow. If something fails (for instance, a schema mismatch or spike in missing data), the system alerts engineers immediately.
Example (CSV Databases):
CSVs → (code/scripts doing cleaning & transformation) → PostgreSQL → Data Science work
1. Extract: You scrape or collect a bunch of CSV files from random websites. This is your raw, messy input.
2. Transform: This is where the actual “data cleaning” happens:
Parsing CSVs
Fixing formats (dates, numbers)
Handling missing values
Deduplicating
Validating schemas
This step is typically done with scripts or tools (Python, Apache Spark, or even SQL transformations).
3. Load: The cleaned data is then inserted into PostgreSQL.
Notes: This process can also be done by using ELT, instead of ETL.
Load raw CSVs into PostgreSQL first
Then transform them inside the database using SQL or tools like dbt
Comparison between traditional ETL vs. modern ETL / ELT
Aspect
Traditional ETL
Modern ETL / ELT stack
Core flow
CSV → Python → PostgreSQL
Sources → Data Lake → Transform → Warehouse
Data sources
Mostly files (CSV, scraped data)
Files, APIs, databases, streams
Storage layer
Directly into PostgreSQL
Data lake like Amazon S3 / Google Cloud Storage
Transformation
Python scripts (pandas, custom logic)
Distributed or SQL-based (Apache Spark, dbt)
Processing scale
Single machine
Distributed across clusters
Loading strategy
ETL (Extract, Transform, Load)
ELT (load first, transform later)
Data volume handling
MB → low GB
GB → TB → PB
Performance bottleneck
CPU / memory of one machine
Cluster size / distributed compute
Reusability
Low (scripts tightly coupled)
High (modular pipelines, reusable models)
Orchestration
Cron jobs / manual runs
Workflow tools (e.g., Airflow)
Data modeling
Done during load
Done after load in warehouse
Schema flexibility
Rigid upfront
Flexible (schema-on-road in lake)
Failure handling
Manual debugging
Built-in retries, logging, monitoring
Cost model
Cheap at small scale
Pay-as-you-scale (storage + compute seperated)
Analytics layer
Same DB handles everything
Dedicated warehouse like Amazon Redshift
Use case fit
Small projects, prototypes
Production systems, large-scale analytics
Notes: Modern stacks do not replace current skills, but reposition those:
Python data cleaning → becomes Spark jobs or dbt models
PostgreSQL knowledge → transfers directly to warehouses
Pipeline logic → move into orchestrators.

## Chapter 1: Introduction To Airflow
What is Airflow?
Airflow is an open-source framework which can be used as an orchestrator.
Example:
What can Airflow actually do?
Orchestrates workflows (DAGs)
Directed Acyclic Graphs – Each DAG is a pipeline of tasks with dependencies, Airflow ensures the workflow runs sequentially and only when conditions are met.
Example: Extract data → Transform it → Load into database → Send report
Schedules jobs
Automates data pipelines
Handle dependencies and retries
Monitoring & logging: Web-based inspection (See task status, view logs, debug pipelines)
Scales execution: Run tasks in parallel and distribute work across multiple workers (Kafka, Celery, Kubernetes, etc.)
What Airflow is not?
Airflow is not a DATA PROCESSING framework.
Airflow is not a REAL-TIME PROCESSING framework.
Airflow is not an ETL framework
Example:
Devices send events to AWS IoT Core, then data lands in Amazon S3. This time Apache Airflow is used to run DAG every 1 minute to:
Check S3 for new files
Read data
Process / aggregate
Push results downstream
In the long run, this practice will lead to hidden latency (delivery – scheduler delay, task queueing + startup time, file listing + read time)  2 – 5+ minutes latency and event-by-event processing loss.
Why not script?
Simple Workflow: Both Airflow & Python-made scripts can excel
Complex Workflow + State: Airflow beats
Failed Scenario: One of the parallel tasks fails to perform, the If branch will be skipped, thus the process stops.
Core Components of Airflow
Metadata DB
Metadata – data about data
E.g: sales_2026.csv → date, product, amount | 2026-01-01, shoes, 100. The metadata could be
File name: sales_2026.csv
Created date: 2026-01-02
Schema: (date: string, product: string, amount: integer)
Source: "E-commerce system"
Owner: "Data team"
Airflow needs to store all the metadata about the DAGs. For instance, DAG runs, schedule, status, task instance, etc.
DAG File Processor: A DAG processor will go to your DAGs folder, parse it and store the serialized DAG {“xyz”: “abc”} into the DB
API Server
Scheduler: Responsible for WHAT & WHEN tasks need to be executed
Executor: Decides the HOW & WHERE tasks need to be run.
Workers: The real layer for execution
Queue
Triggerer
Airflow Architecture
Core Concepts Of Airflow
DAG – Directed Acyclic Graphs
Task Instance – It’s just a single unit of work
Operator - It’s the pre-built template for our tasks. It’s basically tells Airflow what of type task we are running.

## Chapter 2: Linear DAG, Parsing & Versioning
How DAGs are synced?
Implementation
Preliminaries:
.venv/Scripts/Activate
docker compose up -d (Open)
docker exec -it airflow-postgres-1 psql -U airflow -d airflow
docker compose down (Close)
Implementation (Task 1 → Task 2 → Task 3):
Notes: DAGs are versioned by their code (Git). Each run is tied to
A specific execution date / logical date
The DAG structure at the time it ran (does not always snapshot the code per run)
Results:

## Chapter 3: Operators & DAGs Syncing
Definition: Operators are the building blocks of a workflow (DAG). Each operator represents a single task (e.g., running a script, querying a database, or sending an email).
Bash Operators: A specific operator used to run shell commands, which lets you execute any command you’d normally run in a terminal.
Running a .sh script
Using echo, cp, wget, etc.
Triggering CLI tools
E.g:
Two Ways to Declare Tasks in Airflow
Decorator-based (TaskFlow API)
This is the modern, cleaner approach using Python decorators:
Here you can define the use of task by using @task.bash, rather than @task. This will return a bash command string.
Direct Operator Instantiation
This is the older, more explicit method:
Key Differences
Decorator style:
More Pythonic and concise
Easier data passing between tasks
Preferred in newer DAGs
Direct operator style:
More explicit and flexible
Still widely used, especially in legacy DAGs

## Chapter 4: XCOMs (Cross-Communications)
Definition: XCOMs are a built-in mechanism that let tasks share small pieces of data with each other. Since Airflow tasks are designed to be isolated, XCOMs act as a lightweight messaging system between them.
What are they doing?
The store key – value pairs in Airflow’s metadata database
Used for passing small data (not large datasets)
Typically accessed via:
xcom_push() → send data
xcom_pull() → retrieve data
Two common ways to set up communication
Return values
If you are using the TaskFlow API (@task decorator), whatever a task returns is automatically pushed to XCOM. It’s considered to be the cleanest and most modern approach.
What happens:
extract() returns a value
Airflow automatically stores it in XCom
That value is passed downstream as an argument
Using kwargs
In traditional operators (like PythonOperator), you use **kwargs to interact with XCOM manually via the task instance (ti). This method is more flexible, but also more verbose
What happens:
You explicitly push data using xcom_push
You explicitly pull data using xcom_pull
Key differences
Method
Ease of use
Explicit control
Recommended
Return values
⭐⭐⭐⭐
Low
For modern usage
kwargs + XCOM
⭐⭐
High
Use for complex DAGs
Remarks
XComs are not meant for large data (use external storage instead)
Data is serialized (JSON by default)
Each XCom is tied to a specific task instance

## Chapter 5: Parallel Tasks
Definition: Parallel tasks are tasks that can run at the same time within a DAG (Directed Acyclic Graph), as long as their dependencies don’t block them. It helps improving the speed and efficiency.
Implication: After Task 1 being accomplished, Task 2 → 4 are executed concurrently (i.e., both of them depend on Task 1). The previous tasks must be at finished state before running Task 5 or the execution stops.
Implementation
Task 1 – Extract Task
Task 2, 3 & 4 – Transform Respective Data In Dictionary (Run in parallel)
Task 5 – Load Data (Only perform after concurrent tasks all completed)
Define Dependencies
Result:

## Chapter 6: Conditional Branches
Definition: Conditional branching = if-else logic in Python (let a DAG choose different execution paths at runtime)
How does it work: Airflow provides special operators
BranchPythonOperator (classic way)
@task.branch decorator (modern Airflow 2.X way)
The branching function must return:
a task_id (string), or
a list of task_ids
Those tasks will run; all others downstream are marked skipped.
Example (Conditional Branches + Parallel Tasks)
Modification from previous example (Chapter 5)
Add weekend_flag onto dictionary – Set it as false
Add extra task for if-else handling (no_load_task >< load_task)
Create the decider node
Updated Task Dependencies
Result:

## Chapter 7: Scheduling Presets
Definition: Scheduling presets = built-in shortcuts for common cron schedules in Airflow. They make it faster and less error-prone to define when your workflows should run.
Components: start_date (Required), end_date (Optional), catchup (Optional), schedule → Presets (Required)
Common Airflow Scheduling Presets
Preset
Meaning
@once
Run only once
@hourly
Every hour
@daily
Once per day (midnight)
@weekly
Once per week
@monthly
Once per month
@yearly
Once per year
@continuous
Run immediately after previous run finishes
None
No schedule (manual trigger only)
Example
is_paused_upon_creation: Specifies if the dag is paused when created for the first time. If the dag exists already, this flag will be ignored. If this optional parameter is not specified, the global config setting will be used.
Cron Syntax = a 5-field string that tells Airflow exactly when to run a DAG
Cron Format
Common Examples
Cron expression
Meaning
0 * * * *
Every hour
0 0 * * *
Every day at midnight
30 9 * * *
Every day at 09:30
0 0 * * 0
Every Sunday
0 0 1 * *
First day of every month
*/15 * * * *
Every 15 minutes
Worked Example
Result:
Delta Trigger = “run this DAG every X amount of time (e.g., every 03 minutes, every 2 hours)”
How does it work?
Instead of schedule="0 * * * *" # cron (every hour at minute 0)
We use: from datetime import timedelta; schedule = timedelta(hours = 1) → “Run this DAG every 1 hour after the previous session”
Difference between Cron VS. Delta
Cron (fixed clock time) – Runs at exactly: 01:00, 02:00, 03:00; Anchored to the clock
Delta (relative interval) – Run every 1 hour; Anchored to start date (or actual clock standing)
Worked Example
Result:

## Chapter 8: Incremental Load & Jinja Template
Incremental Load: only process new or changed data since the last successful run
Incremental Load Concept:
Load rows where updated_at > last_loaded_timestamp
Load only today’s partition
Load only files added since previous run
CDC (Change Data Capture)
Airflow itself does not do incremental loading automatically. Instead, you implement the logic inside tasks / operators.
Common Pattern:
Source DB/API/File → Find last successful watermark → Query only new records → Load into warehouse → Update watermark
Jinja Templates: Airflow supports Jinja templating in many operators. Useful built-in variables:
Variable
Meaning
{{ ds }}
Execution date (YYYY-MM-DD)
{{ ts }}
Timestamp
{{ prev_ds }}
Previous execution date
{{ next_ds }}
Next execution date
{{ data_interval_start }}
Start of schedule window
{{ data_interval_end }}
End of schedule window
{{ macros.ds_add(ds, 1) }}
Add days
Example:
Note: Why data_interval_start/end is better?
Older tutorials: WHERE updated_at >= ‘{{ ds }}’
Modern Airflow: {{ data_interval_start }}, {{ data_interval_end }}
Because:
Works correctly for hourly / daily schedules
Timezone aware
Aligns with scheduler windows
Avoids overlaps / gaps
Incremental Load Using Last Watermark (optional but production-grade)
Step 1: Store Last Loaded Timestamp
Step 2: Use it in SQL

## Chapter 9: Special Schedules – Events
Definition: Special schedules usually use
Custom timetables
Dataset events
Event-driven scheduling
Hybrid trigger logic
Example:
Run only on trading days
Run after another dataset updates
Run on the last workday of month
Run after file arrival
Run every 3rd Friday
Run after Kafka/S3/db events
Types of Event / Special Scheduling
Cron / Time-based Scheduling
Standard Scheduling: schedule = “0 12 * * *” – Runs everyday at noon
Good for predictable intervals
Timetable-Based Scheduling (Custom Logic)
Airflow allows custom timetable classes, which are considered as “special schedules”
You can define:
holidays
business days
complex intervals
irregular schedules
Dataset/Event-Driven Scheduling
Modern Airflow supports datasets.
A DAG can start when another DAG produces a dataset.
This is true event-driven orchestration.
Implementation

## Chapter 10: Assets
Definition
Assets (called Datasets before Airflow 3.0) are a way to model data dependencies between DAGs instead of relying on cron schedules.
An asset represents a logical piece of data, such as:
an S3 file
a Snowflake table
a Kafka topic
a machine learning model
a business event
When one DAG updates an asset, another DAG can automatically trigger based on that update.
Why Assets Matter
Traditional: schedule="@daily"
Asset-based scheduling: schedule=[customer_table]
This means “Run this DAG when the customer_table asset is updated”, which enables data-aware orchestration.
Core Concepts
Concept
Meaning
Asset
Logical data entity
Asset Event
Update notification
Producer
Task/DAG emitting asset
Consumer
DAG depending on asset
URI
Unique identifier
outlets
Declares produced assets
inlets
Declares consumed assets
Multiple Assets
A single task can emit multiple assets
Example
Dependent Asset
Result

## Chapter 11: Inherited DAG Orchestration
Objective: Designing DAGs so that common orchestration logic, configuration, or task patterns are reused across multiple workflows instead of duplicated.
Airflow itself does not have a first-class “DAG inheritance” feature, but teams commonly implement inheritance-like patterns in Python because DAGs are just Python objects.
Implementation:
Parent Orchestrator:
First DAG Orchestrator:
Seocnd DAG Orchestrator:
Result:
