import pymssql
import csv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read values from .env
server     = os.getenv("DB_SERVER")
port       = int(os.getenv("DB_PORT", 1433))
database   = os.getenv("DB_DATABASE")
username   = os.getenv("DB_USERNAME")
password   = os.getenv("DB_PASSWORD")
csv_file   = os.getenv("CSV_FILE")
table_name = os.getenv("DB_TABLE")

# Connect to SQL Server
conn = pymssql.connect(
    server=server,
    user=username,
    password=password,
    database=database,
    port=port
)
cursor = conn.cursor()

# Open CSV and prepare insert statement
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  # First row = column names

    columns = ', '.join(headers)
    placeholders = ', '.join(['%s'] * len(headers))
    insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    for row in reader:
        cursor.execute(insert_sql, row)

conn.commit()
print(f"✅ Data inserted from {csv_file} into table {table_name}")

cursor.close()
conn.close()
