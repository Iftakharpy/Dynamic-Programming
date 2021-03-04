# return if any combination of nums can add up to the target num
# nums are greater than 0

# optimized

def can_sum_memo(target, nums, memo={}):
    # checking memo
    # print(target, nums, memo)
    if target in memo:
        return memo[target]

    # base cases
    if target < 0:
        return False
    if target == 0:
        return True

    for num in nums:
        if can_sum_memo(target-num, nums , memo):
            memo[target] = True
            return True
    else:
        memo[target] = False
        return False



# Unlike js, python caches the memo.
# So we should put empty memo to avoid false possitives.
print(can_sum_memo(7,[2, 3], {}))
print(can_sum_memo(7,[5, 3, 4, 7], {}))
print(can_sum_memo(7,[2, 4], {}))
print(can_sum_memo(8,[2, 3, 5], {}))
print(can_sum_memo(300,[7, 14], {}))
