import pandas as pd
import MySQLdb

import pandas.io.sql as psql


# setup the database connection.  There's no need to setup cursors with pandas psql.


db=MySQLdb.connect( user='root', passwd='password', db='babbles')

# create the query
query = "select * from message_table_copy"

# execute the query and assign it to a pandas dataframe
df = psql.read_sql(query, con=db)
# close the database connection
db.close()

#print(df['Message_Original'])

df.to_csv(r'C:\Users\karan\PycharmProjects\sentiment\Data_Dump.csv')