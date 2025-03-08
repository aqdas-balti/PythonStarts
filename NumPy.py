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
a+3
print(a)

a = [a%3==0]
print(a)

values = np.random.randn(3,3)
print(values)

data = np.array([['cat','dog','cat'],['dog','dog','cat'],['cat','cat','dog']])
print(data)
#Check karna ka cat ka corresponding ko si values genegarte ho ari ha
print(values[data=='cat'])

arr5 = np.random.randn(4,4)
print(arr5)
print("alag")
arr6=np.round(arr5,2)
print(arr6)
print("ALLLL")
print(arr6[::,0:3])

#Maximum values of array from two arrays
m1=np.array([1,2,3,4,5])
m2=np.array([1,3,4,6,7])
print(np.maximum(m1,m2))

l1=np.arange(9).reshape(3,3)
print(l1)

l2=np.arange(6).reshape(3,2)
print(l2)

#We can't two different shapes of array
# B=l1*l2
# print(B)

#We can calculate dot product of it
print("Dot Product")
print(np.dot(l1,l2))
#Same as upper
print(l1.dot(l2))
#Convert into transpose (row into column and vice versa)
print("Transpose")
print(l1.T)
print(l2.T)
#Infer the dimension from 2 to three or three to 2 etc
print("Infer the Dimension")
print(l1)
print()
print(l2.reshape(3,-1))
print("Merging two Data Sets or arrays")
print(np.concatenate((l1,l2),axis=1))

print("Horizenta Stack")
# print(np.hstack(l1,l2))

# print("Vertical Stack")
# # print(np.hstack(l1,l2))
