import numpy as np
Aarray = np.array([1,2,3,4,5,6])
print("Array using NumPy is :",Aarray)
x = np.arange(16)
print('Arrays are:',x)
print(type(x))
print(np.size(x))
print(np.shape(x))#1D array
x1 = x.reshape(4,4)
print(f'2D Array: {x1}')
print(x1[3,3])
x1[1:,::2]=20
print(x1)
print(x1.max())
print(x1.max(axis=0))#Yea column ma say max value uthaye ga
print(x1.max(axis=1))#Yea row ma say max value uthaye ga
arr=np.arange(16).reshape(4,4)#np.arange() single integer leta hai aur reshape(rows, cols) ke saath use hota hai.
print(arr)
arr1=np.zeros((4,4))# np.zeros() aur np.ones() jaise functions tuple (rows, cols) format mein likhne chahiye.
print(arr1)
arr1=np.ones((4,4))
print(arr1)

arr2 = np.empty([2,4,4])
print(arr2)

arr3 = np.full([2,3], 44)
print(arr3)
#Convert list into array
ls=[22,"python",'Location',4.4]
print(ls)
arr4 = np.array(ls)
print(arr4)

print(arr2.ndim)

#broadcasting
a = np.arange(1, 10, 1).reshape(3,3) 
print(a)
b = np.arange(1, 10, 1).reshape(3,3) 
print(b)
Mul = a*b
print(Mul)
Sub = a-b
print(Sub)
Boolean = a>b
print(Boolean)