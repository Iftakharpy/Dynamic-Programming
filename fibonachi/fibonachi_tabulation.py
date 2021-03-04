# inefficient memory usage
def fib_tabulo(n):
    table = [0]*(n+1)
    table[1] = 1
    
    for i in range(2, n+1):
        if i<=n:
            table[i] = table[i-1] + table[i-2]
    else:
        return table[n]



# Caution: Don't run this.
# Your pc will hang!
print(fib_tabulo(999999999)) 

