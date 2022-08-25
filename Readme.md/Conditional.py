#!/usr/bin/env python
# coding: utf-8

# ### See Your Grade

# In[26]:


marks=int(input("Enter the Obtained Marks "))
if marks>=80 :
    print("your Grade is A")
elif marks>=60 and marks<80 :
    print("your Grade is B")
elif marks>=50 and marks<60 :
    print("your Grade is C")
elif marks>=45 and marks<50 :
    print("your Grade is D")
elif marks>=25 and marks<45 :
    print("your Grade is E")
else :
    print("your Grade is F")


# ### Salary with Bonus

# In[38]:


salary=int(input("Enter Your salary : "))
period=int(input("Enter Your Service Period : "))
if period>=5 :
    salary=((salary*5)//100)+salary
    print("Your Salary with 5% Bonus is :",salary)
else :
    print("You are not Eligible for Bonus")


# ### Square or Not

# In[40]:


length=int(input("Enter the Lenth of a Rectangle : "))
width=int(input("Enter the Width of a Rectangle : "))
if length==width :
    print("It is a Square")
else :
    print("It is Not a Square")


# ### Who is the Oldest and Youngest

# In[44]:


x=int(input("Enter the age of 1st Person : "))
y=int(input("Enter the age of 2nd Person : "))
z=int(input("Enter the age of 3rd Person : "))
if x>y and x>z :
    print("1st Person is the Oldest")
elif y>x and y>z :
    print("2nd Person is the Oldest")
elif z>x and z>y :
    print("3rd Person is the Oldest")
if x<y and x<z :
    print("1st Person is the Youngest")
elif y<x and y<z :
    print("2nd Person is the Youngest")
elif z<x and z<y :
    print("3rd Person is the Youngest")


# ### Celsius to Fahrenheit

# In[58]:


c=int(input("Enter the Temperature in Celsius is : "))
f=int((c*(9/5))+32)
print("The Temperature in Fahrenheit is : ",f,"°F")


# In[ ]:




