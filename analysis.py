import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data=[]
#open csv file and read data
with open('data.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        for i in range(len(row)):
            data.append(row[i])

#remove ( and ) from data
for i in range(len(data)):
    data[i]=data[i].replace('(','')
    data[i]=data[i].replace(')','')

#convert data to integer arrays
for i in range(len(data)):
    data[i]=data[i].split(',')
    for j in range(len(data[i])):
        data[i][j]=int(data[i][j])
        
# print(data[0][0])
df = pd.DataFrame(data)
df = df.pivot(index=0, columns=1, values=2)
print(df)
df.to_csv('analysis.csv')
sns.heatmap(df)
plt.show()