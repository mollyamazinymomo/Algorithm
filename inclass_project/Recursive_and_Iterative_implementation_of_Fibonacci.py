import time
import pandas as pd

def fibonacci(position):
  p=position
  if p<=1:
    return p
  
  num=fibonacci(p-1)+fibonacci(p-2)
  return num

def fibonacci1(position):
  p=position
  list=[0,1]
  if p>=2:
    for i in range(1,p,1):
      new_num=list[i]+list[i-1]
      list.append(new_num)
  return list[p]

'''
print("Please choose one algorithm you want to compute fibonacci list by serial number: \n1.Recursive\n2.Iterative\n")
a1=input("Your choice:\n")
a1=int(a1)

x=input("Please input a position you want to find in febonacci list\n")
x=int(x)

if a1==1:
  start=time.time()
  F1=fibonacci(x)
  end=time.time()
  t1=round(end-start,8)
  print("The number of position",x,"is",F1)
  print("The time it take to compute was",t1,"seconds")

elif a1==2:
  start=time.time()
  F2=fibonacci1(x)
  end=time.time()
  t2=round(end-start,8)
  print("The number of position",x,"is",F2)
  print("The time it take to compute was",t2,"seconds")
'''
t=0
i=0
list_1=[]
list_2=[]

while t<60:
  start=time.time()
  F1=fibonacci(i)
  end=time.time()
  t1=round(end-start,8)
  list_1.append(t1)
  if t1>=60:
    break;
  print("The number of position",i,"in recursive fibonacci list is",F1,"take",t1,"seconds to compute")
  i += 1

list1=pd.DataFrame(data=list_1)
list1.to_csv('list1.csv',encoding='gbk')
print("The maximum number recursive algorighm can compute in 60 seconds is",i)

for n in range(0,i,1):
  start=time.time()
  F2=fibonacci1(n)
  end=time.time()
  t2=round(end-start,8)
  list_2.append(t2)
  print("The number of position",n,"in iterative fibonacci list is",F2,"take",t2,"seconds to compute")

list2=pd.DataFrame(data=list_2)
list2.to_csv('list2.csv',encoding='gbk')
