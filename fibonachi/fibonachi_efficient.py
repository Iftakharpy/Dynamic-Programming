def fibonachi(n):
    prev = 0
    curr = 1
    if n<2:
        return curr
    
    for _ in range(n):
        cache = prev
        prev = curr
        curr = cache+prev
    else:
        return curr


print(fibonachi(300000))
