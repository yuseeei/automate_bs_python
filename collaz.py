#!/usr/bin/env python
# coding: utf-8

# In[87]:


def collaz(number):
  if number % 2 == 0:
    a = number / 2
    return a
  elif number % 2 == 1:
    b = number * 3 + 1
    return b


# In[88]:

print('Enter an integer.')
input_str = input()
c = int(input_str)


# In[89]:


while c != 1:
  c = collaz(c)
  print(c)

