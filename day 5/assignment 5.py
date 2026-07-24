import numpy as np
data=np.array([
    [90,90,56],
    [89,80,87],
    [78,76,56],
    [67,89,99]]
)
average=np.mean(data)
print("average marks:",average)

highest=np.max(data)
print("the highest makrs is:",highest)

lowest=np.min(data)
print("the lowest marks is:",lowest)

subject=["math","sst","science"]

for i in range(len(subject)):
   print(subject[i])
   print("avg:",np.mean(data[:,i]))
   print("max:",np.max(data[:,i]))
   print("min:",np.min(data[:,i]))
   
#overall performance
for i in range(len(data)):
   total=np.sum(data[i])
   avg=np.mean(data[i])

   if avg>90:
      performance="very good"
   elif avg>80:
      performance="good"
   elif avg>60:
      performance="ok"
   else:
      performane="need improve"

   print("student",i+1)
   print("total:",total)
   print("avg:",avg)
   print("performane:",performance)
   print()

