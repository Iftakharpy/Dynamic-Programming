# return any combination of nums can add up to the target num
# nums are possitive integers( num >=0 )

# unoptimized

def how_sum(target, nums):
    # base cases
    if target<0:
        return None
    if target==0:
        return []
    
    for num in nums:
        res = how_sum(target-num, nums)
        # if res!=None we have found a way to add upto the target sum
        if res is not None:
            res.append(num)
            return res
    else:
        return None


print(how_sum(12, [5,4,3]))
print(how_sum(7,[2, 3]))
print(how_sum(7,[5, 3, 4, 7]))
print(how_sum(7,[2, 4]))
print(how_sum(8,[2, 3, 5]))
print(how_sum(300,[7, 14]))
