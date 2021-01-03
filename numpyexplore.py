from numpy import *
a=array(['1',2,3,46.0])
print(a)
'''
There are five different ways to create an array
1. array()
2. linspace()
3. logspace()
4. zero()
5. ones()
'''

a=linspace(1,15,15)
print(a)

b=logspace(1,15)
print(b)

c=zeros(5)
print(c)

d=ones(6)
print(d)