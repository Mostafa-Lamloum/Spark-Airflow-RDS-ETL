# Project Description
This project contains a series of Python scripts used to extract, transform, and load data into a target database. The scripts are designed to be executed using the Apache Airflow scheduler, which automates the execution of these tasks based on a defined DAG (Directed Acyclic Graph). The goal of this project is to demonstrate how to use Airflow to automate the ETL (Extract, Transform, Load) process of data.

# Requirements
* Python 3
* Apache Airflow
* Spark
* MYSQL
* AWS RDS DB

For ease of installation, we include the requirements.txt file for our python environment if needed.


# File Structure
* extract_task.py - This script extracts data from a source database and saves it to a CSV file.
* transform_task.py - This script transforms the data in the CSV file and saves the result to another CSV file.
* load_task.py - This script loads the transformed data from the CSV file into a target database.
* load_Rds_task.py - This script loads the transformed data from the CSV file into an RDS database.
* dag_file.py - This script defines a DAG (Directed Acyclic Graph) that runs the extract, transform, and load tasks in the required order.

# Usage
  To run the ETL process, add the dag_file.py to your airflow/example_Dags directory. You will also need to set the connection in Airflow webserver UI , make sure the spark default is set to spark connection type and the host is local[*] . This is done to be able to use the SparkSubmitOperator

  When using Apache Airflow, we need to set up connections to external systems (such as databases) so that the tasks can access those systems. This is done through the Airflow webserver UI under the Admin tab, where you can create and manage connections. In our case, we need to set up a connection to our target database so that the load_task.py and load_Rds_task.py scripts can write to it.

  To use SparkSubmitOperator in Airflow, we need to configure a connection to our Spark cluster. By default, Airflow comes with a connection named spark_default, which we can modify to point to our Spark cluster. The local[*] is used as the host address, which tells Spark to run locally using all available cores on the machine. This is useful for testing and small datasets, but for larger datasets or clusters, we would need to use a different host address.

  SparkSubmitOperator is an Airflow operator used to submit a Spark job to a cluster. It allows us to run Spark jobs from within Airflow, making it easy to integrate with other tasks in a pipeline. When using SparkSubmitOperator, we can configure the Spark job's parameters, such as the class to run, the arguments to pass, and the driver memory. We can also set dependencies on other tasks in the pipeline, so that the Spark job only runs when the necessary input data is available.

# Conclusion
  This project demonstrates how to use Airflow to automate the ETL process of data. By using Airflow, you can easily schedule and monitor data pipelines, making it a powerful tool for data engineering and automation.
