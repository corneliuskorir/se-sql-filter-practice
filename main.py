import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

orders = pd.read_sql(
    """ 
    SELECT *, COUNT(priceEach)
    FROM orderDetails WHERE priceEach >= 200 ;""",
    conn,
)

print(orders)

conn.close()
