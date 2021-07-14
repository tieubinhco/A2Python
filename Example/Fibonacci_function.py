def fib(n):
    "Print a Fibonacci series up to n."
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()

fib(100)

# Fibonacci numbers module
def fib(n): #write Fibonacci up to n
    a,b= 0,1
    while a<n: 
        print(a,end=' ')
        a,b=b,a+b
    print()

def fib2(n): #return Fibonacci up to n
    result=[]
    a,b= 0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result


   
   