def Fibonacci(n):  
    # First Fibonacci number is 0 
    if n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
 
  
print(f'OUTPUT {Fibonacci(1), Fibonacci(2), Fibonacci(3), Fibonacci(4), Fibonacci(5), Fibonacci(6), Fibonacci(7), Fibonacci(8), Fibonacci(9), Fibonacci(10)}')
