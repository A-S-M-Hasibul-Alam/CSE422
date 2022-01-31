# -*- coding: utf-8 -*-
"""422_Lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xeEG6it79DE3GadTPU96o4gDki0bzqcd
"""

import random

identity_number = input("Enter your identity_number: ")
choto_value = int(input("Enter Minimum Value: "))
boro_value = int(input("Enter Maximum Value: "))

TurnNumberAttacker = int(identity_number[0]) #number of turns
#print("number of turns: ",TurnNumberAttacker)
InitialHPDefender = (int(identity_number[len(identity_number)-1]))*10 + int(identity_number[len(identity_number)-2]) #total life of a defender
#print("total life of a defender:",InitialHPDefender)
NumberOfBulletsChoosen = int(identity_number[2]) #branching factor
#print("branching factor:",NumberOfBulletsChoosen)
govirota = 2*TurnNumberAttacker
#print("govirota:",govirota)
NumberOfLeafNodes = NumberOfBulletsChoosen**govirota
#print("NumberOfLeafNodes:",NumberOfLeafNodes)

nodes = []

for i in range(NumberOfLeafNodes):
      nodes.append(random.randint(choto_value,boro_value))


result,count = minimax(0, govirota, -1000000000000000000, 1000000000000000000, True,count)
#print(result)
#print(count)
print("Depth and Branches Ratio is: "+str(govirota)+":"+str(NumberOfBulletsChoosen))
print("Terminal States (leaf node values) are: ",nodes)
print("Left life(HP) of the defender after maximum damage caused by the attacker is ",InitialHPDefender-result )
print("After Alpha-Beta Pruning Leaf Node Comparisons ",count)

def minimax(position, govirota, alpha, beta, maximizingPlayer,count):
  if govirota == 0:
    count = count+1
    return nodes[position], count

  if maximizingPlayer:
    maxEval = -1000000000000000000
    for i in range(NumberOfBulletsChoosen):
      eval,count = minimax(position*NumberOfBulletsChoosen+i, govirota-1, alpha, beta, False, count)
      maxEval = max(maxEval, eval)
      alpha = max(alpha, eval)
      if beta <= alpha:
        break
    return maxEval, count

  else:
    minEval = 1000000000000000000
    for i in range(NumberOfBulletsChoosen):
      eval,count = minimax(position*NumberOfBulletsChoosen+i, govirota-1, alpha, beta, True, count)
      minEval = min(minEval, eval)
      beta = min(beta,eval)
      if beta <= alpha:
        break
    return minEval, count