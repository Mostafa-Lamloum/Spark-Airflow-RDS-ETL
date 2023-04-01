from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator 
from datetime import datetime

# Define default DAG arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 4, 1)
}

# Define the DAG object
dag = DAG('my_spark_etl_dag', default_args=default_args, schedule_interval='@once')

# Define the extract_data SparkSubmitOperator
extract_data = SparkSubmitOperator(
    task_id='extract_data',
    application='path/to/your/extract.py',
    conf={
        'spark.master': 'your_spark_master_url',
        'spark.executor.memory': '2g'
    },
    dag=dag)

# Define the transform_data SparkSubmitOperator
transform_data = SparkSubmitOperator(
    task_id='transform_data',
    application='path/to/your/transform.py',
    conf={
        'spark.master': 'your_spark_master_url',
        'spark.executor.memory': '2g'
    },
    dag=dag)

# Define the load_data SparkSubmitOperator
load_data = SparkSubmitOperator(
    task_id='load_data',
    application='path/to/your/load.py',
    conf={
        'spark.master': 'your_spark_master_url',
        'spark.executor.memory': '2g'
    },
    dag=dag)

# Define the load_rds_data SparkSubmitOperator
load_rds_data = SparkSubmitOperator(
    task_id='load_rds_data',
    application='path/to/your/load_rds.py',
    conf={
        'spark.master': 'your_spark_master_url',
        'spark.executor.memory': '2g'
    },
    dag=dag)

# Set the dependencies between tasks
extract_data >> transform_data >> [load_data, load_rds_data]
