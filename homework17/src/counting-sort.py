import random
import time
import pandas as pd

class CountingSort:
    def __init__(self, input: list):
        count_array = [0] * (max(input) + 1)
        for i in input:
            count_array[i] += 1
        for i in range(1, len(count_array)):
            count_array[i] = count_array[i] + count_array[i-1]
        output_array = [-1] * len(input)
        for i in input:
            index = count_array[i] - 1
            output_array[index] = i
            count_array[i] -= 1
        #return output_array 

df = pd.DataFrame([[0, 0, 0, 0]], columns=['size, rows', 'number range', 'duration, microsec', 'duration per item, microsec'])
        
rdq = 100
rds = [100, 1000, 10000, 100000, 1000000, 10000000]

for i in range(rdq):
    print(i)
    size = random.randint(0, len(rds)-1)
    space = random.randint(0, len(rds)-1)
    l = [random.randint(0, rds[space]) for i in range(rds[size])]
    start_time = time.time()
    CountingSort(l)
    sd = time.time() - start_time
    sdi = sd * 1000000 / rds[size]
    df = pd.concat([df, pd.DataFrame([[rds[size], rds[space], sd, sdi]], columns=['size, rows', 'number range', 'duration, microsec', 'duration per item, microsec'])])
print(df.sort_values(by='duration per item, microsec', ascending=False).head(20))