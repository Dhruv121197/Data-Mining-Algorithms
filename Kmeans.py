import random
import matplotlib.pyplot as plt

def meann(ds):
  means = []
  space = len(ds[0])
  for i in range(space):
    val = 0
    for j in range(len(ds)):
      val = val + ds[j][i] 
    means.append((val*1.0)/len(ds))
  return means


def dissq(x1,x2):
  d = 0
  space = len(x1)
  for i in range(space):
    d = d + (x1[i]-x2[i])**2
  return d


def kmeans(ds, k):
  centre = random.sample(ds, k)
  cluster = [ [] for i in range(k) ]
  
  
  
  for i in range(len(ds)):
    if ds[i] in centre:
      cluster[centre.index(ds[i])].append(ds[i])
    else:
      min_dis_cluster = 0
      min_dis = dissq(centre[0], ds[i])
      for j in range(1,len(centre)):
        if min_dis > dissq(centre[j], ds[i]):
          min_dis = dissq(centre[j], ds[i])
          min_dis_cluster = j
      cluster[min_dis_cluster].append(ds[i])
    
  
  
  t = 5000#number of iterations
  
    
  for i in range(t):
   
    for w in range(len(centre)):
      centre[w] = meann(cluster[w])
    
    
    
    for j in range(len(ds)):
      flag = False
      
      index = -1
      for it in range(len(cluster)):
        if ds[j] in cluster[it]:
          index = it
          break
        
      min_dis_cluster = index
      min_dis = dissq(centre[index], ds[j])
      
      for w in range(len(centre)):
        if min_dis > dissq(centre[w], ds[j]):
          min_dis = dissq(centre[w], ds[j])
          min_dis_cluster = w
          
      if index!=min_dis_cluster:
        flag = True
        cluster[index].remove(ds[j])
        cluster[min_dis_cluster].append(ds[j])
        
        break
  return cluster




li = [[2,10], [2,5], [8,4], [5,8], [7,5], [6,4], [1,2], [4,9]]

ans  = kmeans(li, 3)
ans2 = kmedoid(li, 3)
col = ['r', 'b', 'g']
index = 0
for item in ans:
  x = []
  y = []
  for i in range(len(item)):
    x.append(item[i][0])
    y.append(item[i][1])
  plt.scatter(x,y,color = col[index])
  index = index + 1

plt.show()

index = 0

for item in ans2:
  x = []
  y = []
  for i in range(len(item)):
    x.append(item[i][0])
    y.append(item[i][1])
  plt.scatter(x,y,color = col[index])
  index = index + 1

plt.show()

