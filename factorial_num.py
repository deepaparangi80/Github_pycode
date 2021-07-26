# program to find factorial of a number
# 0!=1
n = int(input('Enter n:'))

if(n<0):
    print('invalid number')
elif(n==0):
    print('factorial of 0 is 1')
else:
    val = 1
for i in range(1,n+1):
          val = val * i
print('factorial of {} is {}'. format(n,val))       


