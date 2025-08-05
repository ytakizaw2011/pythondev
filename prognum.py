def Fib_seq(num):
    if num <= 2:
        return 1
    
    return Fib_seq(num - 2) + Fib_seq(num - 1)