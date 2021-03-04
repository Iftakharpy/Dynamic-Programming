from pprint import pp

def best_sum_tabulo(target, nums):
    table = [None]*(target+1)
    table[0] = []

    for i in range(target):
        if table[i]!=None:
            for num in nums:
                idx = i+num
                if idx<=target:
                    insert_arr = [*table[i], num]
                    if table[idx] == None:
                        table[idx] = insert_arr
                    elif len(table[idx])>len(insert_arr):
                        table[idx] = insert_arr
    else:
        pp(table)
        return table[target]

print(best_sum_tabulo(7, [5, 3, 4, 7]))
print(best_sum_tabulo(8, [2, 3, 5]))
print(best_sum_tabulo(8, [1, 4, 5]))
print(best_sum_tabulo(100, [1, 2, 5, 25]))
