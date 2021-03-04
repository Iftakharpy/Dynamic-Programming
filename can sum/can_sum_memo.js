// optimized

const can_sum = (target, nums, memo={}) => {
    console.log(target, nums, memo)
    if (target in memo) return memo[target]
    if (target<0) return false
    if (target===0) return true

    for (let num of nums){
        if (can_sum(target-num, nums, memo) === true){
            memo[target] = true
            return true
        }
    }
    memo[target] = false
    return false
}



// js does not cache the memo.
// So we don't need to put empty memo.
console.log(can_sum(7,[2, 3]))
console.log(can_sum(7,[5, 3, 4, 7]))
console.log(can_sum(7,[2, 4]))
console.log(can_sum(8,[2, 3, 5]))
console.log(can_sum(300,[7, 14]))
