import sqlite3

conn = sqlite3.connect('news.db')

conn.execute('''CREATE TABLE IF NOT EXISTS NEWS
         (ID            INT PRIMARY KEY     NOT NULL,
         COMPANY           TEXT             NOT NULL,
         INDUSTRY          TEXT             NOT NULL);''')

#NOTE: you cannot insert this exact line twice
#If you just want to see the content, comment below statement out
# conn.execute('''INSERT INTO NEWS (ID, COMPANY, INDUSTRY) \
#                         VALUES (1, 'Apple', 'Tech'),
#                                (2, 'Google', 'Tech')''')

conn.commit()

cursor = conn.execute("SELECT ID, COMPANY, INDUSTRY from NEWS")
for row in cursor:
   print("ID = ", row[0])
   print("COMPANY = ", row[1])
   print("INDUSTRY = ", row[2])