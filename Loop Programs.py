#!/usr/bin/env python
# coding: utf-8

# ### 1) Print python 10 times

# In[1]:


i=1
while i<=10:
    print("Python")
    i=i+1


# ### 2) Print 1-10

# In[2]:


i=1
while i<=10:
    print(i)
    i=i+1


# ### 3) Print Sum of 1st 10 numbers

# In[3]:


num = 10
sum_of_numbers = 0
while(num > 0):
    sum_of_numbers += num
    num -= 1
print("The sum is", sum_of_numbers)


# ### 4) Print Sum of n Numbers

# In[6]:


num=int(input('enter the value '))
sum_of_numbers = 0
while num > 0:
    sum_of_numbers += num
    num -= 1
print("The sum is", sum_of_numbers)


# ### 5) Table of a Number

# In[7]:


a=int(input("enter table number "))
#b=int(input("enter the number to which table is to printed "))
i=1
while i<=10:
    print(a,"x",i,"=",a*i)
    i=i+1


# ### 6) Factorial of a Number

# In[8]:


num = int(input("enter a number: "))
 
fac = 1
i = 1
 
while i <= num:
    fac = fac * i
    i = i + 1
 
print("factorial of ", num, " is ", fac)


# ### 7) Even Numbers between 1-100

# In[9]:


i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i = i + 1


# ### 8) Palindrome or Not

# In[11]:


num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


# ### 9) Print number in Reverse Order entered by the user

# In[12]:


n=int(input("Enter a number:"))
while n>0 :
    print(n)
    n-=1    


# ### 10) How many number of digits in the given number

# In[13]:


n= int(input("Enter any number "))
c=0
while n>0 :
    n=n//10
    c=c+1
print("Total number of digits in the given number is ",c)


# In[ ]:




