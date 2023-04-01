# ETL Automation using Apache Airflow, Spark and MySQL and AWS RDS

# Project Description:
This project demonstrates how to automate the ETL process using Apache Airflow, Spark, and MySQL. The ETL process involves extracting data from a source database, transforming the data, and then loading it into a target database. Apache Airflow is used to schedule and monitor the ETL tasks, while Spark is used for data processing and MySQL for storing the data. 

# Requirements

    * MySQL
    * Spark
    * PySpark
    * Airflow
    * Amazon RDS

# Installation

    Clone this repository onto your local machine:

    bash

    git clone https://github.com/Mostafa-Lamloum/Spark-Airflow-RDS-ETL


# Project Steps
* Set up your environment by following the steps in Envrionment Setup Folder
* Import desired dataset to your MYSQL database 
* Edit your python scripts for the tasks and the dag scheduler with your required transformations
* Setup your AWS RDS
* Start Spark master and workers using , start-master.sh, and start-worker.sh spark://localhost:7077    
* Start airflow webserver and airflow scheduler from within your environment
* Execute your dag and go to localhost:8080 to observe your tasks running.



# Usage

To use this ETL pipeline, follow the steps outlined in the Installation section above. Once you have set up your environment variables and installed the necessary dependencies, you can run the pipeline by executing the dag_file.py script.

# Troubleshooting 
## If start-master.sh or start-worker.sh are not working   
* Make sure you setup your environment variables properly in the bashrc file 
* If your spark directory is in a protected directory, open the terminal in that directory and use sudo bash start-master.sh



# Contributions

Contributions are always welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.

