# to print the first N prime numbers

print("Prime Numbers")
n = int(input("Enter Number:"))
i=1
if n <=0:
    print("please enter a number greater than 0")
else:
    for _ in range(2*n):
        if i%2==0:
            print(i, end= ' ')
        i+=1