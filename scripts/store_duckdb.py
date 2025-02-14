import duckdb

# Define the absolute path to the data folder
db_path = "C:/Users/HELEN/BigData_Assignment/data/car_sales.duckdb"
csv_path = "C:/Users/HELEN/BigData_Assignment/data/cleaned_car_sales.csv"

# Connect to DuckDB (creates a database file if it doesn't exist)
conn = duckdb.connect(db_path)

# Load cleaned CSV into DuckDB
conn.execute(f"CREATE OR REPLACE TABLE car_sales AS SELECT * FROM read_csv_auto('{csv_path}', header=True)")

# Validate data insertion
row_count = conn.execute("SELECT COUNT(*) FROM car_sales").fetchone()[0]
print(f"✅ Data successfully stored in DuckDB! Total rows: {row_count}")
