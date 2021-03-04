def factorial_memo(n, memo={}):
    if n<=1:
        return 1
    memo[n] = factorial_memo(n-1, memo)*n
    return memo[n]



print(factorial_memo(997))