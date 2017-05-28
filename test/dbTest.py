import sqlite3 as sqlite


db = sqlite.connect('../rss.sqlite')
cursor = db.execute("select * from rss_fetch_record")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("password = ", row[2],"\n")

