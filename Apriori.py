import math
def Apriori(df, min_support):
  
  supp = math.ceil(((min_support*1.0)/len(df.index)))
  C = []
  L = []
  
  for column in df:
    sup_cnt = sum(df[column])
    C.append([[column],sup_cnt])
    if sup_cnt >= supp:
      L.append([[column], sup_cnt])
    
  dfC = pd.DataFrame(C, columns = ['Itemset', 'Support Count'])
  dfL = pd.DataFrame(L, columns = ['Itemset', 'Support Count'])
  print(dfC)
  print()
  print(dfL)
  
  k = len(df.columns)
  
  for index in range(2, k):
    C_index = []
    L_index = []
    for i in range(len(L)-1):
      for j in range(i+1,len(L)):
        li = L[i][0] + L[j][0]
        li = list(dict.fromkeys(li))
        li.sort()
        indices = list(range(0, len(df.index)))
        for item in li:
          indices1 = [ii for ii, x in enumerate(df[item]) if x]
          indices = list(set(indices) & set(indices1))
        sup_cnt = len(indices)
        if(len(li) == index):
          C_index.append([li, sup_cnt])
          
        if(sup_cnt >= supp and len(li) == index):
          L_index.append([li,sup_cnt])
    L = L_index
    import itertools
    C_index.sort()
    L_index.sort()
    C_index = list(C_index for C_index,_ in itertools.groupby(C_index))
    L_index = list(L_index for L_index,_ in itertools.groupby(L_index))
    dfC = pd.DataFrame(C_index, columns = ['Itemset', 'Support Count'])
    dfL = pd.DataFrame(L_index, columns = ['Itemset', 'Support Count'])
    print(dfC)
    print()
    print(dfL)

import pandas as pd

from mlxtend.preprocessing import TransactionEncoder

dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

Apriori(df, 0.1)
