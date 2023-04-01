# Data Engineering ETL Pipeline using Spark, PySpark, Airflow and Amazon RDS

This project is an ETL pipeline that extracts data from MySQL using Spark and PySpark for data transformation and then loads it onto Amazon RDS for storage. The pipeline is fully automated using Airflow, ensuring the smooth flow of data from the source to the destination.
Requirements

    MySQL
    Spark
    PySpark
    Airflow
    Amazon RDS

Installation

    Clone this repository onto your local machine:

    bash

    git clone https://github.com/Mostafa-Lamloum/Spark-Airflow-RDS-ETL

Install the necessary dependencies:

    bash

    pip install -r requirements.txt

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
