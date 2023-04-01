from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Set up SparkSession
spark = SparkSession.builder.appName('load_job').getOrCreate()

# Read data from a CSV file into a Spark DataFrame
df = spark.read.csv('path_to_your_transform_file.csv', header=True)

# Write data to a MySQL database
df.write \
    .format('jdbc') \
    .option('url', 'jdbc:mysql://<database_host>:<port>/<database_name>') \  ## If you are using local host and a MYSQL Database then it would localhost:3306 
    .option('dbtable', '<table_name>') \
    .option('user', '<username>') \
    .option('password', '<password>') \
    .mode('overwrite') \
    .save()

# Write data to a CSV file
df.toPandas().to_csv('path_to_your_load_output_file.csv', index=False)

# Stop the SparkSession
spark.stop()

