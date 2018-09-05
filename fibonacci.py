

####Fibonacci


## prints the Fibonacci sequence of n numbers


##Recursive

def Fib(n):
    if n  > 1:
        return Fib(n-1) + Fib(n-2)
    else:
        return n


n = 5
for i in range(n+1):
    print(Fib(i))


#iterative, works well
def Fib_2(n):
    prev = 0
    curr = 1
    print("{}".format(prev))
    for i in range(n):
        print("{}".format(curr))
        curr = prev + curr
        prev = curr - prev


print("-----------------")
Fib_2(5)

