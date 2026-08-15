import pandas as pd
from sqlalchemy import create_engine

# MySQL details
username = "postgres"
password = "yugesh"
host = "localhost"
port = 5432
database = "customer_behavior"

# Create MySQL connection
engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

print("MySQL connected successfully!")

# Read CSV file
df = pd.read_csv("customer_shopping_behavior.csv")

print(df.head())

# Upload DataFrame to MySQL
table_name = "customer"

df.to_sql(
    table_name,
    engine,
    if_exists="replace",
    index=False
)

print(f"Data successfully loaded into table '{table_name}'")

# Read data from MySQL
data = pd.read_sql(
    "SELECT * FROM customer LIMIT 5",
    engine
)

print(data)                  