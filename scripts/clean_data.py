       from pyspark.sql import SparkSession
       from pyspark.sql.functions import col, trim, lower

       # Initialize Spark Session
       spark = SparkSession.builder \
       .appName("CarSalesCleaning") \
       .getOrCreate()

       # Load dataset
       file_path = "../data/car_sales_dataset_with_person_details.csv"
       df = spark.read.csv(file_path, header=True, inferSchema=True)

       # 1️⃣ Standardizing Column Names (Removing spaces)
       df = df.withColumnRenamed("First Name", "First_Name") \
              .withColumnRenamed("Last Name", "Last_Name") \
              .withColumnRenamed("Mileage", "Mileage_KM") \
              .withColumnRenamed("Address", "Customer_Address")

       # 2️⃣ Remove Duplicates       
       df = df.dropDuplicates()


       # 3️⃣ Standardizing Text Columns (trim spaces, lowercase)
       df = df.withColumn("Brand", trim(lower(col("Brand")))) \
              .withColumn("Model", trim(lower(col("Model")))) \
              .withColumn("Color", trim(lower(col("Color")))) \
              .withColumn("Condition", trim(lower(col("Condition")))) \
              .withColumn("First_Name", trim(lower(col("First_Name")))) \
              .withColumn("Last_Name", trim(lower(col("Last_Name")))) \
              .withColumn("Country", trim(lower(col("Country"))))

       # 4️⃣ Save cleaned data as CSV for further processing
       df.coalesce(1).write.mode("overwrite").option("header", "true").csv("../data/cleaned_car_sales")

       print("✅ Data Cleaning Completed! Cleaned dataset saved as 'cleaned_car_sales.csv'.")
       print df.columns