import sqlite3
import os.path
from pathlib import Path

s = os.path.dirname(__file__)
p = Path(s).parent.parent.parent.joinpath("database")

class DataBaseManager():
    db_raw_path = str(p) + os.path.sep + "detail.db"

    def __init__(self)->None:
        pass

    @classmethod
    def search_power_frequency(cls,min_power:float, max_power:float, min_frequency:float, max_frequency:float)->None:
        con = sqlite3.connect(cls.db_raw_path)
        cur = con.cursor()
        cur.execute("select * from Frequency where frequency BETWEEN :min_f AND :max_f AND power BETWEEN :min_p AND :max_p;", 
                    {"max_f":max_frequency,"max_p":max_power, "min_f":min_frequency,"min_p":min_power})
        result = cur.fetchall()
        con.commit()
        con.close() # not effecient

        return result

