import numpy as np
import matplotlib.pyplot as plt

dataset=[12, 10, 11, 14, 76, 103, 13,15,12,16,17,11,16,25, 110, 20, 23, 27,19, 18,10,13,78, 15,14,20,28,32,87,
23,25,19,22,28,17,27,80,15, 18, 22, 20,25,82,27,21,12,15,18,90,108,28,150]
sortedData=sorted(dataset)
plt.hist(dataset)

# z score
n=len(dataset)
q1_index=n//4
if (n%4==0):
  q1=(sortedData[q1_index]+sortedData[q1_index-1])/2
else :
  q1=sortedData[q1_index]

q3_index=3*n//4
if (n%4==0):
  q3=(sortedData[q3_index]+sortedData[q3_index-1])/2
else :
  q1=sortedData[q3_index]

if n % 2 == 0:
    median1 = sortedData[n//2]
    median2 = sortedData[n//2 - 1]
    q2 = (median1 + median2)/2
else:
    q2 = sortedData[n//2]

# iqr and boundaries
iqr=q3-q1
lower=q1-(1.5*iqr)
upper=q3+(1.5*iqr)
print (lower, upper)

print(q1,q2,q3)

outliers=[x for x in sortedData if x<lower or x>upper]

# plot the box pot
plt.figure(figsize=(10,6))
plt.boxplot(dataset,vert=False,patch_artist=False)
plt.title("boxplot")
plt.xlabel("Value")
plt.yticks([1],["Dataset"])

for outlier in outliers:
  plt.annotate(str(outlier),xy=(outlier,1),xytext=(outlier,1.1),arrowprops=dict(facecolor='red',shrink=0.05))

plt.grid(True)
plt.show()