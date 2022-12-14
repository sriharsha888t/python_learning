import math
raw_data=[20.4,float('NaN'),int(5),30.5,15.0]
filtered_data=[]
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)