# optimized

# moves only (right or down)
def grid_memo(m, n, memo={}):
    # checking if the value is memoized
    if (m,n) in memo:
        return memo[(m,n)]
    if (n,m) in memo:
        return memo[(n,m)]
    
    # base cases
    if m==0 or n==0:
        return 0
    if m==1 and n==1:
        return 1
    
    # saving the value to memo
    memo[(m,n)] = grid_memo(m-1, n, memo) + grid_memo(m, n-1, memo)
    return memo[(m,n)]




# Unlike js, python caches the memo. If we want to cache in js we should make the memo global in js.
# So, we should put empty memo to avoid false possitives.
# But here we don't have a two arguments but these recalulated.
# So, it would be better not to put empty memo so we don't recalculate.
# Because the previously calculated value will be cached. 
# Therefore, we won't need to recalculate the values again.

# print(grid_memo(500,500))
print(grid_memo(0,0))
print(grid_memo(1,0))
print(grid_memo(1,1))
print(grid_memo(1,10))
print(grid_memo(3,4))
print(grid_memo(8,10))
print(grid_memo(10,6))
print(grid_memo(18,18))