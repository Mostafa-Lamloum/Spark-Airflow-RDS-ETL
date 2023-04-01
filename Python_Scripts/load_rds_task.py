
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.appName('load_job').getOrCreate()

# Read data from a CSV file into a Spark DataFrame
df = spark.read.csv('/path/to/transformed/file.csv', header=True)

# Write data to a target database table
df.write \
  .format('jdbc') \
  .option('url', 'jdbc:your_database_url') \  ## jdbc:mysql://database_endpoint_from_rds.com:port  , default port is 3306
  .option('dbtable', 'your_database_table_name') \ # your_database.your_table_name
  .option('user', 'your_database_username') \
  .option('password', 'your_database_password') \
  .mode('overwrite') \
  .save()

# Write data to a CSV file
df.toPandas().to_csv('/path/to/output_file.csv', index=False)

# Stop the SparkSession
spark.stop()
