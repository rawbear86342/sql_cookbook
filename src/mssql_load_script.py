import pymssql

# Connect to the database
conn = pymssql.connect(
    server='your_server',
    user='your_username',
    password='your_password',
    database='your_database',
    port=1433
)

cursor = conn.cursor()

# Load the SQL script file
with open('init_script.sql', 'r') as file:
    sql_script = file.read()

# Split statements by semicolon (you can make this smarter if needed)
statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip()]

# Execute each statement
for stmt in statements:
    cursor.execute(stmt)

# Commit the transaction
conn.commit()

print("SQL script executed successfully.")

cursor.close()
conn.close()
