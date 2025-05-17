import numpy as np
from time import time

arr = np.arange(20,dtype=np.float64)
id:str = str(time())
json_dict = {id: list(arr)}

print(type(json_dict))
lst:list[str] = json_dict.get(id)
print(len(lst))
print(type(lst[0]))

