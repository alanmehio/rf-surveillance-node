import os.path
import sqlite3
from pathlib import Path


#print(type(os.pardir))
#print(os.pardir)
#print(os.path.dirname(__file__))
#print(os.path.dirname(__file__))
s = os.path.dirname(__file__)
p = Path(s)
print(p.parent)
#os.path

#s  = os.path.join(os.path.dirname(__file__), os.pardir,'test.yaml')
#print(os.path.realpath("../" + os.path.dirname(__file__)))

#con = sqlite3.connect(os.path.join(os.path.dirname(__file__)) + "tutorial.db")
#cur = con.cursor()
#cur.execute("CREATE TABLE movie(title, year, score)")



#conn = sqlite3.connect(os.path.realpath('../data/test.db'))