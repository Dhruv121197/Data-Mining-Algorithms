import random
def dissq(x1,x2):
  d = 0
  space = len(x1)
  for i in range(space):
    d = d + (x1[i]-x2[i])**2
  return d

def medoid2(ds):
  means = []
  space = len(ds[0])
  for i in range(space):
    val = 0
    for j in range(len(ds)):
      val = val + ds[j][i] 
    means.append((val*1.0)/len(ds))
  medoid = []
  mindis = 100000000000
  for i in range(len(ds)):
    dis = dissq(means, ds[i])
    if(dis < mindis):
      mindis = dis
      medoid.append(ds[i])
  return medoid[len(medoid)-1]

def manhattan(x1,x2):
  d = 0
  space = len(x1)
  for i in range(space):
    d = d + abs(x1[i]-x2[i])
  return d




def kmedoid(ds, k):
  centre = random.sample(ds, k)
  cluster = [ [] for i in range(k) ]
  
  
  
  for i in range(len(ds)):
    if ds[i] in centre:
      cluster[centre.index(ds[i])].append(ds[i])
    else:
      min_dis_cluster = 0
      min_dis = manhattan(centre[0], ds[i])
      for j in range(1,len(centre)):
        if min_dis > manhattan(centre[j], ds[i]):
          min_dis = manhattan(centre[j], ds[i])
          min_dis_cluster = j
      cluster[min_dis_cluster].append(ds[i])
    
  
  
  t = 5000#number of iterations
  
    
  for i in range(t):
    #print(cluster)
    for w in range(len(centre)):
      centre[w] = medoid2(cluster[w])
    
    #print(centre)
    
    for j in range(len(ds)):
      index = -1
      for it in range(len(cluster)):
        if ds[j] in cluster[it]:
          index = it
          break
        
      min_dis_cluster = index
      min_dis = manhattan(centre[index], ds[j])
      #print("init_min_dis",min_dis)
      #print("index",index)
      for w in range(len(centre)):
        if min_dis > manhattan(centre[w], ds[j]):
          min_dis = manhattan(centre[w], ds[j])
          min_dis_cluster = w
          #print("mindis = ", min_dis)
      if index!=min_dis_cluster:
        cluster[index].remove(ds[j])
        cluster[min_dis_cluster].append(ds[j])
        #print("hello",ds[j])
        break
     
    
      
    
    
      
      
  return cluster

import turtle
pen = turtle.Turtle()
pen.speed(0.8)
pen.dot()
turtle_window = turtle.Screen() 
def topdown(ds, x, y, length):
  if(len(ds) == 1):
      return
  cluster = kmedoid(ds, 2)
  flat_list = []
  for sublist in cluster:
    for item in sublist:
        flat_list.append(item)
  
  pen.up()
  pen.goto(x,y)
  pen.write(flat_list)
  pen.down()
  
  pen.seth(0)
  pen.right(90)
  pen.forward(50)
  pen.left(90)
  pen.forward(100-length)
  pen.right(90)
  pen.forward(50)
  pen.dot()
  x1, y1 = pen.pos()
  pen.backward(50)
  pen.left(90)
  pen.backward(200-2*length)
  pen.right(90)
  pen.forward(50)
  pen.dot()
  x2, y2 = pen.pos()
  
  
  topdown(cluster[0], x1, y1, length+40)
  topdown(cluster[1], x2, y2, length+40)
  

li = [[2,10], [2,5], [8,4], [5,8], [7,5], [6,4], [1,2], [4,9]]
topdown(li, 0, 0, 0)
turtle_window.exitonclick()


