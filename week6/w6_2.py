def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)
def fibo_1(n):
    if n<=1:
        return n
    prev, current = 0,1
    for _ in range(2,n+1):
        prev, current = current, prev+current
    return current
def fibo_2(n,fi={0:0,1:1}):
    if n not in fi:
        fi[n]=fibo_2(n-1)+fibo_2(n-2)
        print(fi)
    return fi[n]
        
