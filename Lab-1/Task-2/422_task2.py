# -*- coding: utf-8 -*-
"""422_task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gx1G62VcUgWBVNInFEyzzsUdKdTmqCiD
"""

input=open('input1.txt','r')
lines= input.readlines()

from queue import Queue
counter_queue = Queue()

g_matrix = []
count = 0
for line in lines:
  count = count+1
  if (count==1):
    row = int(line.strip())
  elif(count==2):
    coloumn = int(line.strip())
  else:
    g_matrix.append(line.split())



#print(row)
#print(coloumn)
#print(g_matrix)

print(g_matrix)

visited = [[0]*coloumn for _ in range(row)]

print (visited)

for i in range(row):
  for j in range (coloumn):
    if ((g_matrix[i][j]) == "A"):
      visited[i][j] = 1
      st = []
      st.append(i)
      st.append(j)
      counter_queue.put(st)

print (counter_queue.queue)
queue_size = counter_queue.qsize()
print (queue_size)

while not counter_queue.empty():
  for i in range(row):
    for j in range (coloumn):
      if ((g_matrix[i][j]) == "A" and visited[i][j]==1):
        counter_queue.get()
        if(i>-1 and i<row and j>-1 and j<coloumn):
          if(i-1>-1):
            if(visited[i-1][j]==0 and g_matrix[i-1][j]=="H"):
              visited[i-1][j] = 1
              g_matrix[i-1][j] = "A"
              st = []
              st.append(i-1)
              st.append(j) 
              counter_queue.put(st)
              
          if(i+1<row):
            if(visited[i+1][j]==0 and g_matrix[i+1][j]=="H"):
                visited[i+1][j] = 1
                g_matrix[i+1][j] = "A"
                st = []
                st.append(i+1)
                st.append(j) 
                counter_queue.put(st)
                
          if(j-1>-1):
            if(visited[i][j-1]==0 and g_matrix[i][j-1]=="H"):
                visited[i][j-1] = 1
                g_matrix[i][j-1] = "A"
                st = []
                st.append(i)
                st.append(j-1) 
                counter_queue.put(st)
                
          if(j+1<coloumn):
            if(visited[i][j+1]==0 and g_matrix[i][j+1]=="H"):
                visited[i][j+1] = 1
                g_matrix[i][j+1] = "A"
                st = []
                st.append(i)
                st.append(j+1) 
                counter_queue.put(st)

print (counter_queue.queue)
print (counter_queue.qsize())

print(g_matrix)

human_counter = 0
for i in range(row):
  for j in range (coloumn):
    if ((g_matrix[i][j]) == "H"):
      human_counter = human_counter+1

print(human_counter)