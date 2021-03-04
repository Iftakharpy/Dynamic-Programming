# return the combination of nums can add up to the target num.
# and the length of the returned array is smallest.
# nums are possitive integers( num >=0 )

# optimized
import math

def best_sum(target, nums, memo={}):
    # checking memo
    if target in memo:
        return memo[target]
    
    #base cases
    if target<0:
        return None
    if target == 0:
        return []
    
    # initial result
    length = math.inf
    best_solution = None
    
    for num in nums:
        new_solution = best_sum(target-num, nums, memo)
        if new_solution is not None:
            # if the current soultions length is smaller than previous then re asign the pervious one
            if len(new_solution)<length:
                best_solution = [*new_solution, num]
                length = len(best_solution) 
                memo[target] = best_solution
    else:
        memo[target] = best_solution
        return best_solution



# print(best_sum(12, [1,2,6,5, 4,3],{}))
# print(best_sum(7,  [1, 2, 3],{}))
# print(best_sum(7,  [1, 5, 3, 4, 7],{}))
# print(best_sum(7,  [2, 4],{}))
# print(best_sum(8,  [2,1, 3, 5],{}))
# print(best_sum(300,[7, 14, 4],{}))
print(best_sum(7, [5, 3, 4, 7], {}))
print(best_sum(8, [2, 3, 5], {}))
print(best_sum(8, [1, 4, 5], {}))
print(best_sum(100, [1, 2, 5, 25], {}))