from pyspark.sql import SparkSession

# Set the path for the extracted data
path_to_extract_file = 'path/to/extract_file.csv'

# Create a SparkSession
spark = SparkSession.builder.appName('extract_job').getOrCreate()

# Read data from a MYSQL database into a Spark DataFrame
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:mysql://your_host:your_port") \  # replace your_host and your_port with your database connection details
    .option("user", "your_username") \ # replace your_username with your database username
    .option("password", "your_password") \ # replace your_password with your database password
    .option("query", "select * from your_database.your_table") \ # replace your_database and your_table with your actual database and table names
    .load()

# Write data to a CSV file
df.toPandas().to_csv(path_to_extract_file)

# Stop the SparkSession
spark.stop()
