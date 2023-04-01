# Project Description
This project contains a series of Python scripts used to extract, transform, and load data into a target database. The scripts are designed to be executed using the Apache Airflow scheduler, which automates the execution of these tasks based on a defined DAG (Directed Acyclic Graph). The goal of this project is to demonstrate how to use Airflow to automate the ETL (Extract, Transform, Load) process of data.

# Requirements
* Python 3
* Apache Airflow
* Spark
* MYSQL
* AWS RDS DB


# File Structure
* extract_task.py - This script extracts data from a source database and saves it to a CSV file.
* transform_task.py - This script transforms the data in the CSV file and saves the result to another CSV file.
* load_task.py - This script loads the transformed data from the CSV file into a target database.
* load_Rds_task.py - This script loads the transformed data from the CSV file into an RDS database.
* dag_file.py - This script defines a DAG (Directed Acyclic Graph) that runs the extract, transform, and load tasks in the required order.

# Usage
  To run the ETL process, add the dag_file.py to your airflow/example_Dags directory. You will also need to set the connection in Airflow webserver UI , make sure the spark default is set to spark connection type and the host is local[*] . This is done to be able to use the SparkSubmitOperator

  Once the DAG is set up, Airflow will automatically execute the tasks in the defined order based on the schedule you set. You can monitor the progress of the tasks in the Airflow UI and view the logs to troubleshoot any errors.

# Conclusion
  This project demonstrates how to use Airflow to automate the ETL process of data. By using Airflow, you can easily schedule and monitor data pipelines, making it a powerful tool for data engineering and automation.
