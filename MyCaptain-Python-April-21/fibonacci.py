a=0
b=1
n=int(input("Enter the value of n:"))
print("Fibonacci series:")
print(a,b,end=" ")
for i in range (2,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

