from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

# Initialize a Spark Session
spark = SparkSession.builder \
    .appName("CarSalesDataProcessing") \
    .config("spark.sql.shuffle.partitions", "8") \
    .getOrCreate()

# Define file path
file_path = "../data/car_sales_dataset_with_person_details.csv"

# Load dataset into PySpark DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Print schema to understand the structure
df.printSchema()

# Show first 10 rows
df.show(10)

# Count total rows
print(f"Total Rows: {df.count()}")

# Check for missing values
df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).show()
