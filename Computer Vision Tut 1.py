#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import numpy as np


# In[47]:


a=cv2.imread(r"nature.jpg")


# In[8]:


loc=r"nature.jpg"


# In[9]:


#Display image
from PIL import Image
im=Image.open(loc)
im.show()


# In[10]:


#Conversion to grayscale
b=[[sum(i)//3 for i in j]for j in a]


# In[13]:


b.shape


# In[12]:


b=np.array(b,dtype="uint8")


# In[14]:


type(a)


# In[15]:


type(b)


# In[16]:


data=Image.fromarray(b)


# In[17]:


data.save("grey.jpg")


# In[18]:


img=Image.open("grey.jpg")


# In[19]:


#Grayscale
img.show()


# In[20]:


#dimensions of the image
b.shape


# In[21]:


a.shape


# In[22]:


#channel red
red=[[[i[0],0,0] for i in j] for j in a]
red=np.array(red,dtype="uint8")
dr=Image.fromarray(red)
dr.save("red.jpg")
im=Image.open("red.jpg")
im.show()


# In[23]:


#channel green
green=[[[0,i[1],0] for i in j] for j in a]
green=np.array(green,dtype="uint8")
dr=Image.fromarray(green)
dr.save("green.jpg")
im=Image.open("green.jpg")
im.show()


# In[24]:


#channel blue
blue=[[[0,0,i[2]] for i in j] for j in a]
blue=np.array(blue,dtype="uint8")
dr=Image.fromarray(blue)
dr.save("blue.jpg")
im=Image.open("blue.jpg")
im.show()


# In[28]:


im_new=[[a[i][j] for j in range(1486,1586)] for i in range(1102,1202)]


# In[29]:


im_new=np.array(im_new,dtype="uint8")


# In[30]:


im_new.shape


# In[31]:


#mid 100 pixels
im_new=Image.fromarray(im_new)
im_new.save("im_new.jpg")
im=Image.open("im_new.jpg")
im.show()


# In[32]:


array=np.zeros((2304,3072,3),dtype="uint8")


# In[34]:


for i in range(0,2304,10):
    for j in range(0,3072,20):
        array[i][j]=a[i][j]


# In[36]:


#10 and 20
im_new=Image.fromarray(array)
im_new.save("im_new.jpg")
im=Image.open("im_new.jpg")
im.show()


# In[48]:


b=a[::-1][:][:]


# In[50]:


#flip vertically
im_new=Image.fromarray(a)
im_new.save("im_new.jpg")
im=Image.open("im_new.jpg")
im.show()


# In[54]:


#image histogram
import matplotlib.pyplot as plt
n=cv2.imread(r"nature.jpg",0)
plt.hist(n.ravel(),256,[0,256])
plt.show()

