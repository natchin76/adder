"""
Created on Wed Nov  6 00:23:37 2019
Function file that adds two numbers/strings/lists...
Arbitrary number of inputs are allowed
@author: CHINTAN
"""
def add(*s):
    a=0
    for i in range(len(s)):
        a=a+s[i]
    return(a)        
        
    
print(add(1,3,4))
