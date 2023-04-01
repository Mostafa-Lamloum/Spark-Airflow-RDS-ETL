from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col 

# Create a SparkSession
spark = SparkSession.builder.appName('transform_job').getOrCreate()

# Read data from a CSV file into a Spark DataFrame
df = spark.read.csv("path/to/your/extract/file.csv", header=True)

# Replace empty strings with None and drop any rows with null values
df2 = df.replace(to_replace= '' , value= None)
df2=df2.dropna()

# Drop the "region_url" and "url" columns
df2 = df2.drop('region_url', 'url')

# Extract only the first character from the "cylinders" column
df2 = df2.withColumn('cylinders', split(col('cylinders'), ' ').getItem(0))

#Convert the dtype of cylinders to int for aggregation and analytics purposes 
df2 = df2.withColumn('cylinders', df['cylinders'].cast('int'))


# Write data to a CSV file
df2.toPandas().to_csv('path/to/your/transform/file.csv', index=False)

# Stop the SparkSession
spark.stop()
