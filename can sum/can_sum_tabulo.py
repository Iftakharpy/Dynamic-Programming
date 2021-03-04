

def can_sum_tabulo(target, nums):
    table = [False]*(target+1)
    table[0] = True

    for i in range(target):
        if table[i]:
            for num in nums:
                if i+num<=target:
                    table[i+num] = True
    else:
        return table[target]


print(can_sum_tabulo(10, [10]))
print(can_sum_tabulo(12, [10, 2, 3]))
