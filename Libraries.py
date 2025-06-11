# Maths Library
import math
x=math.sqrt(25)
print(x)

import math as m
print(m.sqrt(5))

import numpy as np
np.array([1,2,3])
print(np.array([1,2,3]))

import numpy as np  # Short form se use karna better hai
num = np.arange(10)  # 0 se 9 tak array banayega
print(num)

from math import sqrt
print(sqrt(35))

from math import sqrt as sq
print(sq(25))

from math import *
print(floor(2.1))#2
print(ceil(3.1))#4

'''This is multiple line comments'''

#Classes
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def getcarname(self):
        print(f"The name of a car is: {self.make}")
    def getcarmodel(self):
        print(f"The Model of a car is: {self.model}") 
    def getcaryear(self):
        print(f"The Year of a car is:{self.year}") 
car1 = Car('Honda','City','2025')
car1.getcarname()   
car1.getcarmodel()
car1.getcaryear()