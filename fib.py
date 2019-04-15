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