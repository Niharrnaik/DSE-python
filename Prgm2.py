import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
#basic operation 
print("Array a:",a)
print("Array b:",b)
print("sum of the array a and b:",np.add(a,b))
print("Difference of the array a and b:",np.subtract(a,b))
print("product of the array a and b :",np.multiply(a,b))
print("Division of the array a and b :",np.divide(a,b))
print("Square of the array a and b :",np.sqrt(a))
print("exponential of the array a and b :",np.exp(a))
#Aggregation operations
print("minimum of array a",np.min(a))
print("minmum of array a:",np.max(b))
print("mean of array a:",np.mean(a))
print("standard deviation  of array a:",np.std(b))
