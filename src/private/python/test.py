import psycopg2
import pandas.io.sql as pdsql

params = {
  'dbname': 'clicc',
  'user': 'clicc',
  'password': 'clicc',
  'host': '192.168.99.100',
  'port': 5432
}

# Connect to a PostGIS database
conn = psycopg2.connect(**params)
curs = conn.cursor()

# Build custom SQL query
query = """
    SELECT huc, (ST_ValueCount(ST_Union(ST_Clip(rast,geom)))).* 
       INTO counts 
       FROM nlcd_area, catchment 
       GROUP BY huc; 
    SELECT huc, value, count, (SUM(count) OVER (PARTITION BY huc)) 
        AS sum 
        INTO counts_sum 
        FROM counts;
    SELECT huc, value, (CAST(count AS float) / CAST(sum AS float)) 
        AS fraction 
        FROM counts_sum;
"""

# Execute query and write to pandas data frame
df = pdsql.read_sql(query, conn)

# Print data frame contents
print(df)