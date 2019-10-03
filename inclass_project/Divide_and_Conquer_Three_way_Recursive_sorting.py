def mergesort(arr):
    #if len(arr) <= 1:
      #return arr 
    n=len(arr)
    mid1=n//3
    mid2=n//3*2
    #If there is no control, if len(arr)=2, then the len(arr3) will alsways be 2
    if n%3==2:
      control=1;
    else:
      control=0
    
    if n>1:  
      arr1=mergesort(arr[:mid1])
      arr2=mergesort(arr[mid1:mid2+control])
      arr3=mergesort(arr[mid2+control:])
    else:
      return arr

    return merge(arr1,arr2,arr3)

def mergetwo(left,right) :
  i=0
  j=0
  result=[]
  while i < len(left) and j < len(right):
      if left[i] <= right[j]:
          result.append(left[i])
          i += 1
      else:
          result.append(right[j])
          j += 1
  result += left[i:]
  result += right[j:]
  return result

def merge(arr1,arr2,arr3):
    arr_1=mergetwo(arr1,arr2)
    result=mergetwo(arr_1,arr3)
    return result



x=input("Pleasee input the dataset,use ',' to split\n")
y=x.split(',')
arr=[]
for i in y:
  arr.append(int(i))
print("Before",arr)

result=mergesort(arr)
print("After",result)
