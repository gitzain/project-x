import sqlite3
db = sqlite3.connect('news.db')
db.execute("CREATE TABLE news (id INTEGER PRIMARY KEY, title TEXT NOT NULL, date TEXT NOT NULL, category TEXT, story TEXT NOT NULL)")
db.execute("CREATE TABLE sources (id INTEGER NOT NULL, source TEXT NOT NULL, url TEXT NOT NULL, headline TEXT NOT NULL, story TEXT NOT NULL)")

db.execute("INSERT INTO news (title,date, category, story) VALUES ('Title','18/07/16 12:30:45', 'Business', 'This is a the story')")
db.execute("INSERT INTO news (title,date, category, story) VALUES ('2nd Title','19/07/16 12:10:45','Politics', 'This is the second story')")

db.execute("INSERT INTO sources (id,source,url,headline,story) VALUES (1,'bbc','http://bbc.co.uk','headline for bbc','story for bbc')")
db.execute("INSERT INTO sources (id,source,url,headline,story) VALUES (1,'cde','http://cde.co.uk','headline for cde','story for cde')")
db.execute("INSERT INTO sources (id,source,url,headline,story) VALUES (2,'cnn','http://cnn.com', 'headline for cnn','story for cnn')")
db.commit()