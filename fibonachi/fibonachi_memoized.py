# optimized

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


# Unlike js, python caches the memo. If we want to cache in js we should make the memo global in js.
# So, we should put empty memo to avoid false possitives.
# But here we don't have a single argument
# So, it would be better not to put empty memo.
# Because the previously calculated value will be cached. 
# Therefore, we won't need to recalculate the values again.

print(fib_memo(3))
print(fib_memo(4))
print(fib_memo(5))
print(fib_memo(6))
print(fib_memo(7))
print(fib_memo(8))
print(fib_memo(100))
