import pandas as pd
from sqlalchemy import create_engine

# Read Excel
df = pd.read_excel('Ecommerce_Unclean_Project.xlsx')

# Save CSV
df.to_csv('cleaned_data.csv', index=False)

# MySQL connection
engine = create_engine(
    'mysql+pymysql://root:12345@localhost:3306/ecommerce'
)

# Import DataFrame into MySQL
df.to_sql(
    'ecommerce_cleaned',
    con=engine,
    if_exists='replace',
    index=False
)

print("Data imported successfully!")