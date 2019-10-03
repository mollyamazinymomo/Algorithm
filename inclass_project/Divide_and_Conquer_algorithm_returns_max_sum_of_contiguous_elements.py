def Maxsum(num_list):
  left=0
  right=len(num_list)-1
  Maxsum=divideconquer(num_list,left,right)
  return Maxsum

def divideconquer(num_list,left,right):
  if left==right:
    return num_list[left]
  
  center=(left+right)//2

  Maxsum_left=divideconquer(num_list,left,center)
  Maxsum_right=divideconquer(num_list,center+1,right)

  Sum_left=num_list[center]
  Sum_borderleft=num_list[center]
  position1=center
  for i in range(center-1,left-1,-1):
    Sum_left += num_list[i]
    if Sum_left>Sum_borderleft:
      position1=i
      #print(position1)
      Sum_borderleft=Sum_left
      print()

  Sum_right=num_list[center+1]
  Sum_borderright=num_list[center+1]
  position2=center+1
  for i in range(center+2,right+1):
    Sum_right += num_list[i]
    if Sum_right>Sum_borderright:
      position2=i
      #print(position2)
      Sum_borderright=Sum_right
  
  Max_border=Sum_borderleft+Sum_borderright
  #print(Maxsum_left,Maxsum_right,Max_border)
  MaxSum=max(Maxsum_left,Maxsum_right,Max_border)
  #print(position1,position2)
  print("The start point of sublist with max sum is:",position1,"\nThe end point of sublist with max sum is:",position2)
  print("The sublist with max sum is",num_list[position1:position2+1])
  
  return MaxSum

x=input("Please input a list of number, use ',' to split\n")
y=x.split(',')
num_list=[]
for i in y:
  num_list.append(int(i))
print("The list input is",num_list)

Maxsum=Maxsum(num_list)

print("The sublist's largest sum is",Maxsum)
