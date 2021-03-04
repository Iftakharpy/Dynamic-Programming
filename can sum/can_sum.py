# return if any combination of nums can add up to the target num
# nums are possitive integers( num >=0 )

# unoptimized

def can_sum(target, nums):
    if target < 0:
        return False
    if target == 0:
        return True

    for num in nums:
        if can_sum(target-num, nums):
            return True
    else:
        return False


print(can_sum(7,[2, 3]))
print(can_sum(7,[5, 3, 4, 7]))
print(can_sum(7,[2, 4]))
print(can_sum(8,[2, 3, 5]))
print(can_sum(300,[7, 14]))