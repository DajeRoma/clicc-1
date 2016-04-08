
# coding: utf-8

# In[2]:

###########################################################################
# Package Imports and Database Connection Settings
###########################################################################

# Package imports
import psycopg2
import pandas.io.sql as pdsql

# Set database connection parameters
params = {
  'dbname': 'clicc',
  'user': 'clicc',
  'password': 'clicc',
  'host': '192.168.99.100',
  'port': 5432
}

# Attempt to connect to a PostGIS database running in docker container
try: 
    conn = psycopg2.connect(**params)
    print('Connected to PostGIS Database')
except: 
    print('Failed to Connect to PostGIS Database')


# In[5]:

###########################################################################
# Task #1
###########################################################################

# Build custom SQL query to compute landuse fractions
queryLF = """
    SELECT huc, 
    (ST_ValueCount(ST_Union(ST_Clip(rast,geom)))).*
       INTO counts 
       FROM landuse, catchments 
       GROUP BY huc; 
    SELECT huc, value, count, 
    (SUM(count) OVER (PARTITION BY huc)) AS sum 
        INTO counts_sum 
        FROM counts;
    SELECT huc, value, count, 
    (@ST_ScaleX(rast) * @ST_ScaleY(rast) * (CAST(count AS float))) AS area, 
    (CAST(count AS float) / CAST(sum AS float)) AS fraction
        FROM landuse, counts_sum
        ORDER BY huc, count;
"""

# Execute query and write to pandas data frame
LF = pdsql.read_sql(queryLF, conn)

# Print data frame contents
print(LF)


# In[8]:

###########################################################################
# Task #2
###########################################################################

# Build custom SQL query to compute mean reach depth
queryRD = """
    SELECT huc, 
    AVG(pdepth) AS mean_depth 
        FROM reaches
        GROUP BY huc
        ORDER BY mean_depth;
"""

# Execute query and write to pandas data frame
RD = pdsql.read_sql(queryRD, conn)

# Print data frame contents
print(RD)


# In[4]:

###########################################################################
# Task #3
###########################################################################

# Build custom SQL query to compute the distribution of landuses per
# soil classification zone
querySG = """
    SELECT huc, muid, 
    ST_Intersection(catchments.geom,soils.geom) AS int_geom
        INTO soils_int
        FROM catchments, soils
        GROUP BY huc, muid, catchments.geom, soils.geom;
    SELECT huc, muid, 
    (ST_ValueCount(ST_Union(ST_Clip(rast,int_geom)))).* AS counts
        INTO counts
        FROM landuse, soils_int
        GROUP BY huc, muid;
    SELECT huc, muid, value, count, 
    (SUM(count) OVER (PARTITION BY muid)) AS sum 
        INTO counts_sum 
        FROM counts;
    SELECT huc, muid, value, count, 
    (@ST_ScaleX(rast) * @ST_ScaleY(rast) * (CAST(count AS float))) AS area, 
    (CAST(count AS float) / CAST(sum AS float)) AS fraction
        FROM landuse, counts_sum
        ORDER BY huc, muid, count;
"""

# Execute query and write to pandas data frame
SG = pdsql.read_sql(querySG, conn)

# Print data frame contents
print(SG)

