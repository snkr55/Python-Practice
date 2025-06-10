
print("Fibonacci Series")
n = int(input("Enter Number:"))

i=0
j=1
if n<=0:
    print("please enter positive number greater than 0")
elif n==1:
    print(i)
elif n==2:
    print(i,j)
else:
    for _ in range(n):
        print(i,end = ' ')
        i, j = j, i + j
        
