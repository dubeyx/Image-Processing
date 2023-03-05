#!/usr/bin/env python
# coding: utf-8

# In[5]:


#AKHIL Dubey - 2020UCO1673

import cv2
import numpy as np


# In[2]:


# Q1
patch = np.array([[56, 170, 184, 129, 95],
                  [112, 91, 94, 95, 157],
                  [86, 182, 77, 125, 69],
                  [167, 163, 142, 111, 190],
                  [71, 189, 34, 149, 50]], dtype=np.uint8)

dx = cv2.Sobel(patch, cv2.CV_32F, 1, 0, ksize=3)
dy = cv2.Sobel(patch, cv2.CV_32F, 0, 1, ksize=3)

print("Input patch:\n", patch)
print("x-gradient:\n", dx)
print("y-gradient:\n", dy)


# In[3]:


# Q2
Ixx = dx * dx
Iyy = dy * dy
Ixy = dx * dy

sum_Ixx = np.sum(Ixx)
sum_Iyy = np.sum(Iyy)
sum_Ixy = np.sum(Ixy)

Harris_matrix = np.array([[sum_Ixx, sum_Ixy],
                          [sum_Ixy, sum_Iyy]])

print("Harris Matrix:\n", Harris_matrix)


# In[4]:


# Q3
eigvals, eigvecs = np.linalg.eig(Harris_matrix)

print("Eigenvalues:\n", eigvals)
print("Eigenvectors:\n", eigvecs)

# Q4
lambda1, lambda2 = eigvals

if lambda1 > lambda2:
    lambda_max = lambda1
    lambda_min = lambda2
else:
    lambda_max = lambda2
    lambda_min = lambda1

threshold = 100000

if lambda_max > threshold:
    print("Edge")
elif lambda_min > threshold:
    print("Corner")
else:
    print("Flat surface")


# In[ ]:




