import math

def Bubblesort(lst):
  n=len(lst)
  for i in range(0,n):
    for j in range(0,n-i-1):
      if lst[j]>lst[j+1]:
        (lst[j],lst[j+1])=(lst[j+1],lst[j])
  return lst

x=input("Pleasee input the dataset,use ',' to split\n")
y=x.split(',')
arr=[]
for i in y:
  arr.append(int(i))
print(arr)
arr=Bubblesort(arr)

n=len(arr)
arr1=[]
arr2=[]
for i in range(n):
  if i%2==1:
    arr1.append(arr[i])
  else:
    arr2.append(arr[i])
arr3=[]
for i in range(n//2):
  arr3.append(arr2[i]-arr1[i])
d=arr3[0]
for i in range(1,len(arr3)):
  if abs(d-arr3[i])<abs(d+arr3[i]):
    arr1[i],arr2[i]=arr2[i],arr1[i]
    d=d-arr3[i]
  else:
    d=d+arr3[i]
arr4=[]
for i in range(n//2):
  arr4.append(arr1[i]-arr2[i])
minimum_difference=abs(sum(item for item in arr4))
print("The two dataset splited are:",arr2,arr1)
print("The minimum difference will be:",minimum_difference)
