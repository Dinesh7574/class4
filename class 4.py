#!/usr/bin/env python
# coding: utf-8

# In[1]:


#dict
a = {"name": "dinesh" ,"age":20 ,"loc":"chennai"}
print(a.get("name"))
print(a["name"])


# In[2]:


print(a.get("add"))


# In[3]:


a = {"name": "dinesh" ,"age":20 ,"loc":"chennai"}
print(type(a))


# In[4]:


print(isinstance(a,dict))


# In[1]:


a = {"name": "dinesh" ,"age":20 ,"loc":"chennai"}
a["add"]="test"


# In[2]:


a = {"name": "dinesh" ,"age":20 ,"loc":"chennai"}
print(a)


# In[5]:



a["add"]="test"
print(a)


# In[20]:


a = {'name': 'dinesh', 'age': 20, 'loc': 'chennai', 'add': 'test'}
del a["add"]
print(len(a))
print(a)


# In[7]:


print(sorted(a))


# In[22]:



a = {'name': 'dinesh', 'age': 20, 'loc': 'chennai','name':'vishwak'} #it overwrite
print(a)


# In[11]:


print(a.keys())    #it shows keys


# In[12]:


print(a.values())  #it shows values


# In[13]:


print(a.items())  #it shows  both keys and values


# In[14]:


#operator
#arithmetic

a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a**b) #square root
print(a/b)
print(a//b) #floor dividsion it shows quotient
print(a%b)  #modulus it shows reminder


# In[23]:


#assignment operator
a =5
b=6


# In[24]:


#relational
a = 5
b = 2
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)


# In[25]:


#logical operator
#and
print(True and True)         #true
print(True and False)    #false
#or
print(True  or True)   #true
print(True or False)  #true
#not
print( not True)  #false
print(not False)  #true


# In[ ]:




