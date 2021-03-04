# return any combination of nums can add up to the target num
# nums are possitive integers( num >=0 )

# optimized

def how_sum_memo(target, nums, memo={}):
    #checking memo
    if target in memo:
        return memo[target]

    # base cases
    if target<0:
        return None
    if target==0:
        return []
    
    for num in nums:
        res = how_sum_memo(target-num, nums, memo)
        # if res!=None we have found a way to add upto the target sum
        if res is not None:
            res.append(num)
            memo[target] = [*res]
            return res
    else:
        memo[target] = res
        return None


# Python caches the memo.
# So, we have to put empty memo to avoid false possitive.

print(how_sum_memo(7, [2, 3], {}))
print(how_sum_memo(7, [2, 4], {}))
print(how_sum_memo(7,[5,3,4,7], {}))
print(how_sum_memo(8, [2, 3,5], {}))
print(how_sum_memo(12, [5,4,3], {}))
print(how_sum_memo(999,[7,100], {}))
