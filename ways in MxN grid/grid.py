# unoptimized

# moves only (right or down)
def grid(m, n):
    if m<=0 or n<=0:
        return 0
    if m==1 and n==1:
        return 1
    return grid(m-1, n) + grid(m, n-1)


print(grid(3,3))
print(grid(6,4))
print(grid(5,5))
print(grid(9,8))
print(grid(4,3))
print(grid(1,30))
print(grid(10,6))
print(grid(18,18))