📌 Project Overview

This project builds a complete data pipeline for analyzing car sales data. The ETL pipeline extracts, cleans, and processes data before storing it in DuckDB for fast queries and analytics. Finally, insights are visualized using Power BI dashboards to help businesses understand sales trends, brand performance, and customer demographics.

🛠 Tech Stack & Tools Used

✔ Programming Language: Python (Pandas, PySpark)
✔ Database: DuckDB
✔ Visualization: Power BI
✔ Libraries: Pandas, PySpark, DuckDB, Matplotlib
✔ Version Control: GitHub

📊 Power BI Dashboard Insights

🚀 Key Visualizations & Insights:

📈 Car Sales Trends Over Time (Line Chart)

🚗 Top-Selling Car Brands (Bar Chart)

✅ Car Condition Analysis (New vs. Used) (Pie Chart)

💰 Average Car Price by Brand (Column Chart)

🌍 Customer Demographics by Country (Map Visualization)

📌 Full dashboard available in https://app.powerbi.com/links/kw9Z4oRlZX?ctid=1695066a-e388-40d1-8ed5-5d0b28ba9f80&pbi_source=linkShare&bookmarkGuid=3f0e0088-f7d6-4257-973f-13584dbabdc9

📦 ETL Pipeline Process

1️⃣ Extract Phase

✔ Loaded dataset (1M+ rows) using PySpark.

✔ Read raw CSV into a DataFrame for processing.

2️⃣ Transform Phase

✔ Cleaned missing values in Color & Condition.

✔ Created new calculated columns:

Car_Age = Current Year - Manufacturing Year

Price_Category (Low, Medium, High)

Total_Revenue = Price * Quantity Sold

✔ Removed duplicates & formatted data types.

3️⃣ Load Phase

✔ Designed a relational schema and stored processed data in DuckDB.

✔ Ensured optimized query performance for Power BI analysis.

🚀 How to Run This Project?

1️⃣ Clone This Repository

git clone https://github.com/your-username/Car-Sales-Data-Pipeline.git

cd Car-Sales-Data-Pipeline

2️⃣ Install Required Dependencies

pip install pandas pyspark duckdb matplotlib

python scripts/extraction.py   # Extract raw data

python scripts/transform.py    # Clean & transform data

python scripts/load.py         # Load into DuckDB

4️⃣ Open Power BI Dashboard

Navigate to powerbi/Car_Sales_Dashboard.pbix

Open in Power BI Desktop and explore interactive reports.

📬 Contact & Contributions

🔹 Author: Samuel Tekie

💡 Pull requests & feature suggestions are welcome! 🚀
