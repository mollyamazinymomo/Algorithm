def Triad_search(arr,sn,left,right):
    if left>=right:
        return -1
    #decide the two point to divide
    mid1=(right-left)//3+left
    mid2=(right-left)*2//3+left
    #discuss five situation might occur
    if arr[mid1]==sn:
        return mid1
    elif arr[mid2]==sn:
        return mid2
    elif arr[mid1]>sn:
        return Triad_search(arr,sn,left=left,right=mid1)
    elif sn>arr[mid1] and sn<arr[mid2]:
        return Triad_search(arr,sn,left=mid1+1,right=mid2)
    else:
        return Triad_search(arr,sn,left=mid2+1,right=right)

x=input("Pleasee input the dataset,use ',' to split\n")
y=x.split(',')
arr=[]
for i in y:
  arr.append(int(i))
#print(arr)
#specific number
sn=input("Please input the number you want to find\n")
sn=int(sn)

position=Triad_search(arr,sn,0,len(arr))
#print(position)

if position==-1:
  print("There is no such number in the list")
else:
  print("The position of the number",sn," is ",position)
