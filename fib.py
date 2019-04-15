def fibonacciVal(n):
  memo = [0] * (n+1)
  print(memo)
  memo[0], memo[1] = 0, 1
  for i in range(2, n+1):
    memo[i] = memo[i-1] + memo[i-2]
    
  return memo[n]

print(fibonacciVal(3))
def fib(n, memo):
    if memo[n] != None:
        return memo[n]
    elif n <=1:
        memo[n] = n
        return n
    else:
        q = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = q
        return q


def starter():
    my_arr = [None] * 20
    print(fib(5, my_arr))

starter()
