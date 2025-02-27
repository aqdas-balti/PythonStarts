# Functions

def fun():
    print("This is my first function in python")
fun()

def fun(x):
    print(x*2)

fun(2)

def multiply (x):
    result = x * 4
    return result
print(multiply(2))

# Max and Min No's
print("Max Number is:",max(1,2,3,4,5,6,7,8,9)
)

print("Min Number is:",min(1,2,3,4,5,6,7,8,9)
)

# Absolute Numbers
print("Absolute No is:",abs(-5))

# Lists are mutable means we can change the lists:
list = [1,2,3,4,5]
print("Lists are :",list)
print("First index vlaue is:",list[0])
print("From first to 4th values:",list[0:4])# Is ma akhri wali index shamil ni hoti ha
print("Total length of a list before append:",len(list))
list.append("Aqdas")
print("New Lists:",list)
print("Total length of a list after append:",len(list))

#Some useful functions:

print("'Kaito','Islamabad','40'".split(','))

list2 = [2,4,5]
print("Sum:",sum(list2))
#Ye function value ka index return karta hai, lekin agar wo value list mein mojood na ho, to ValueError dega.
print(list2.index(5))#2
#Two dimensional lists list with in list
list3=[list,list2]
print("Two dimensional lists are:",list3)
print(list3[0][0])#1
print(list3[1][0])#2
#Sorting a lists with .sort() and sorted() build in functions/ methods
list4 = [2,1,3,6,5,4,7,8,9]
list4.sort()
print(list4)
print(list3.sort())
list5 = [3, 1, 2]
print(list5)
new_list = sorted(list5)  # Creates a new sorted list
print(new_list)  # Output: [1, 2, 3]
x= range(10)
print(x)
print(x[2])

#Tuples are immutable we can't change the tuple
t = (1,3,2,5,4,8,7,9)
print("Tuples:",t)
print(t[7])
print(t[-5])

#Dictionaries: In this key value pair are availabe
Xdict = {'House_1':'20k', 'House_2':'30k', 'House_3':'40k'}
# print(Xdict["House_1"])
Xdict['House_4']='50k'
# print(Xdict)
#Store list in dictionary
Ydict={} # Define the dictionary before using it
Ydict['another dict']={'House_1':'200k', 'House_2':'300k', 'House_3':'400k'}
# print(Ydict)

# Xdict={} # Define the dictionary before using it
# Xdict['another dict']={'House_1':'200k', 'House_2':'300k', 'House_3':'400k'}
# print(Xdict)

#For Loop
for i in Xdict:
    print(i)
    print(Xdict[i])


x = 5
while(x>0):
    print(x)
    x=x-1

print("Another While")
y = 0
while(y<5):
    print(y)
    y+=1

print("Nested for loop")
ls1 =[1,2,3]
ls2 = [1,2,3]
for i in ls1:
    for j in ls2:
        print('i=',i)
        print('j=',j)
        print ("i*j=",i*j)
