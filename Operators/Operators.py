#!/usr/bin/env python
# coding: utf-8

# ### Membership

# In[3]:


x="Hi I'm Joy"
print('Joy' in x)


# In[4]:


x="Hi I'm Joy"
print('RC' in x)


# In[5]:


x="Hi I'm Joy"
print('is' not in x)


# In[6]:


x="Hi I'm Joy"
print('Hi' not in x)


# ### Bitwaise Operators

# #### AND

# In[9]:


### Bitwise AND - returns 1 if both the bits are 1 else 0
x = 6 # binary form 0110
y = 4 # binary form 0100
print('bitwise AND', x&y)


# #### OR

# In[10]:


# bitwise OR - returns 1 if either of the bits is 1 else 0
x = 6 # binary form 0110
y = 4 # binary form 0100
print('bitwise OR', x|y)


# #### NOT

# In[12]:


# bitwise NOT - returns one's complement of the number
x = 2 # binary form 0010
print('bitwise NOT',~x)


# #### XOR

# In[13]:


# bitwise XOR - returns 1 if one of the bits is 1 and other is 0 else returns false
x = 18 # binary form 10010
y = 6  # binary form 01100
print('bitwise XOR',x^y)


# In[14]:


x = 6 # binary form 00110
print('bitwise right shift',x>>1) #0011
print('bitwise left shift',x<<1)


# In[15]:


import sys
v=23.17
print(id(v))                                    #unique address
print(type(v))                                  #data type of variable
print(sys.getsizeof(v))                         #size of object in bytes
print(v, "is float?", isinstance(v,float))      #isinstance checks data type


# In[ ]:




