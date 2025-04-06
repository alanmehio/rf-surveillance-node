import json

from io import StringIO
from datetime import datetime
import numpy as np

class NumpyComplexEncoder(json.JSONEncoder):

    def default(self, obj)->any:
        
        if isinstance(obj,complex):
            return (obj.real,obj.imag)
        else:
            return None
        


arr = np.arange(10, dtype=np.complex128)
com = np.complex128(2324234,-234234234.445454)
#arr[0] = com
#arr[1] = com
json_str  = json.dumps(arr.tolist(), cls=NumpyComplexEncoder)
'''
 def real(self) -> float64: ...
    @property
    def imag(self) -> float64: ...
'''
print(json_str)
d:dict =  {"samples": json_str,
            "now": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
           
}

result = json.dumps(d)
print(result)
