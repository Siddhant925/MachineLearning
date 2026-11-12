def NonRecursiveFibonacci(num):
    a,b = 0,1
    for i in range(num):
        print(a, end=" ")
        a,b = b,a+b;

def RecursiveFibonacci(num):
    if num <= 1:
        return num
    return RecursiveFibonacci(num-1) + RecursiveFibonacci(num-2)

n = int(input("Enter a number: "))

print("\nFibonacci Series {Recursive}: ", end=" ")
for i in range(n):
    print(RecursiveFibonacci(i), end=" ")

print("\nFibonacci Series {Non-Recursive}: ", end=" ")
NonRecursiveFibonacci(n)
print()