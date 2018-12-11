import os

ori = [2,6,4,4,6,5,8,7,4,1,10,9,6,8,3,6,2,7]
sorted = []
keys = list(range(1,11))
container = dict.fromkeys(keys,0)
for o in ori:
    container[o] = container[o]+1
for key,value in container.items():
    temp_list = [key] * value
    sorted.extend(temp_list)
print(sorted)
