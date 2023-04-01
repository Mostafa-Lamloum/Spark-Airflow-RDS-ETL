# : ETL Automation using Apache Airflow, Spark and MySQL and AWD RDS

# Project Description:
This project demonstrates how to automate the ETL process using Apache Airflow, Spark, and MySQL. The ETL process involves extracting data from a source database, transforming the data, and then loading it into a target database. Apache Airflow is used to schedule and monitor the ETL tasks, while Spark is used for data processing and MySQL for storing the data. 

Requirements

    * MySQL
    * Spark
    * PySpark
    * Airflow
    * Amazon RDS

# Installation

    Clone this repository onto your local machine:

    bash

    git clone https://github.com/Mostafa-Lamloum/Spark-Airflow-RDS-ETL



Set up your environment variables:

    MYSQL_HOST: Hostname for MySQL server
    MYSQL_DATABASE: Name of the MySQL database
    MYSQL_USERNAME: Username for MySQL server
    MYSQL_PASSWORD: Password for MySQL server
    RDS_HOST: Hostname for Amazon RDS instance
    RDS_DATABASE: Name of the Amazon RDS database
    RDS_USERNAME: Username for Amazon RDS instance
    RDS_PASSWORD: Password for Amazon RDS instance

Run the ETL pipeline:

    bash

    python etl_pipeline.py

Usage

To use this ETL pipeline, follow the steps outlined in the Installation section above. Once you have set up your environment variables and installed the necessary dependencies, you can run the pipeline by executing the etl_pipeline.py script.
Contributions

Contributions are always welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.
License

This project is licensed under the MIT License.
