from pprint import pp

def grid_tabulo(n, m):
    if n==0 or m==0:
        return 0
    if n==1 or m==1:
        return 1
    
    table = [[0 for _ in range(m+1)] for x in range(n+1)]
    table[0][1]=1

    for i in range(1,n+1):
        for j in range(1,m+1):
            table[i][j] = table[i-1][j]+table[i][j-1]
    else:
        return table[n][m]


print(grid_tabulo(10,6))
print(grid_tabulo(18,18))
