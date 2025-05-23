import numpy as np
arr = np.array([
    ['id', '796132', '1148512', '87741691', '87910849', '88188296'],
    ['diagnosis', '1', '0', '1', '0', '0'],
    ['fractal_dimension_worst', '0.08701', '0.08006', '0.08255', '0.06484', '0.1118']
])

json_dict = {l[0]: list(l[1:]) for l in arr}

print(type(json_dict))
lst:list[str] = json_dict.get("id")
print(len(lst))
print(type(lst[0]))

'''
{'id': ['796132', '1148512', '87741691', '87910849', '88188296'],
 'diagnosis': ['1', '0', '1', '0', '0'],
 'fractal_dimension_worst': ['0.08701',
  '0.08006',
  '0.08255',
  '0.06484',
  '0.1118']}
'''
