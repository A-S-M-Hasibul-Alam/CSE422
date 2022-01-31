# -*- coding: utf-8 -*-
"""422_Lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1keSYj01bNgZBEsF7E7I5ITdTxC3TUhMn
"""

import numpy as np
import random

row = input("Enter your row numbers: ")
row = int(row)
print(row)

mat = [[0]*2 for _ in range(0,row)]
print(mat)

print("Put your given values")
for i in range (row):
  val = input() #putting value like l,1212
  x = val.split(",",2)
  #print(x[0])
  #print(i)
  mat[i][0] = (x[0])
  if (x[0] == 'l'):
    mat[i][1] = int(x[1])*-1
  else:
    mat[i][1] = int(x[1])

print(mat)

#declaring population

start_manushjon = 8

mutation_threshold = 0.2

manushjon = np.random.randint(0, 2, (start_manushjon, row))

print(manushjon)

#fitness function
#fit = []
def fitness_fn (manushjon):

  fit_value = 0
  for i in range (len(manushjon)):
    fit_value = fit_value + manushjon[i]*mat[i][1]
    #fit.append(fit_value)
    #print(fit_value)
  return fit_value
#print(fit)

#select function

def selector_fn(manushjon):
  baccha = random.choice(manushjon)
  
  return baccha

#crossover function
def crossover_fn(baccha1, baccha2):
  num = random.randint(0,len(baccha1)-1)
  
  return baccha1[0:num]+baccha2[num:len(baccha1)]

#mutation function

def mutation_fn(baccha):
  index_num = random.randint(0,row)
  #print(index)
  index_val = random.randint(0,2)
  baccha[index_num] = index_val
  
  return baccha

#Genetic Algorithm

def genetic_algo(manushjon, fitness_fn):
  max_iterate = 10000

  while max_iterate>0:
    notun_manushjon = []

    for i in range (len(manushjon)):
      x = selector_fn(manushjon)
      y = selector_fn(manushjon)
      baccha = crossover_fn(x,y)
    
    random_num = random.uniform(0,1)

    if(random_num < mutation_threshold):
      baccha = mutation_fn(baccha)
    
    notun_manushjon.append(baccha)
    
    manushjon = notun_manushjon

  if(fitness_fn(manushjon)==0):
    print(manushjon)
  else:  
    print("-1")

manushjon =np.random.randint(0, 2, (start_manushjon, row))
genetic_algo(manushjon, fitness_fn)