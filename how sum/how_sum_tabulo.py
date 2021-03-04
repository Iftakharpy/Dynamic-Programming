from pprint import pp

def how_sum_tabulo(target, nums):
    table = [None]*(target+1)
    table[0] = []

    for i in range(target):
        if table[i]!=None:
            for num in nums:
                idx = i+num
                if idx<=target:
                    table[idx] = [*table[i], num]

    else:
        return table[target]
    

print(how_sum_tabulo(10, [7,6,10]))
