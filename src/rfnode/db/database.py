import sqlite3
import os.path
from pathlib import Path

class RowDataBaseManager():
    def __init__(self):
        pass
    def getDB
    def createDB():
        s = os.path.dirname(__file__)
        p = Path(s).parent.parent.parent.joinpath("database")
        db_path = str(p) + os.path.sep + "row.db"

#https://docs.python.org/3/library/sqlite3.html



#print(s)
p = Path(s)
p = p.parent.parent.parent
p = p.joinpath("database")
print(str(p))
db_path = str(p) + os.path.sep + "row.db"
conn = sqlite3.connect(db_path)

#print(os.path.realpath())
#os.path

#s  = os.path.join(os.path.dirname(__file__), os.pardir,'test.yaml')
#print(os.path.realpath("../" + os.path.dirname(__file__)))

#con = sqlite3.connect(os.path.join(os.path.dirname(__file__)) + "tutorial.db")
#cur = con.cursor()
#cur.execute("CREATE TABLE movie(title, year, score)")



#conn = sqlite3.connect(os.path.realpath('../data/test.db'))