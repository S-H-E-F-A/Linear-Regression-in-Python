X1=0
X2=0
Y1=0
XY=0
number_list = []
number_list2 = []
n = int(input("Enter total Data Points' Number: "))#Enter an Integer Number,e.g. 5

for i in range(1, n+1):
    print("X%d:"%i)
    item = int(input())
    number_list.append(item)
for j in range(1, n+1):
    print("Y%d:"%j )
    item = int(input())
    number_list2.append(item)

for i in range(0, n):
   X1=  X1 + number_list[i] 
   X2=  X2 + number_list[i]*number_list[i]
   # print("baal2->",number_list[i])
   Y1=  Y1 + number_list2[i]
   XY=  XY + number_list[i]*number_list2[i]

b = (n*XY - X1*Y1)/(n*X2 - X1*X1)
m = (Y1 - b*X1)

print("m = ", m)
print("b = ", b)
print("Finding best parameters for linear regression, y = mx+b : Y=%dx+%d" %(m,b))




  
