#ARMSTRONG
import math

t = cnt = 0

n = int(input("Enter a number: "))

n1 = n
n2 = n

while n!=0:
    n = n//10
    cnt+=1
while n1!=0:
    r = n1%10
    t = t+ pow(r,cnt)
    n1 = n1//10
if t == n2:
    print("Given number ",n2,'is ARMSTRONG\n')
else:
    print("Given number ",n2,'is NOT ARMSTRONG\n')
    
