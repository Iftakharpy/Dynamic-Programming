# return if the string can be coonstructed by any combination of words

from typing import List
# optiomized

def can_construct_memo(string: str, words: List[str], memo={}) -> bool:
    # checking memo
    if string in memo:
        return memo[string]
    
    # base case
    if string=="":
        return True

    for word in words:
        if string.startswith(word):
            if can_construct_memo(string.removeprefix(word), words, memo):
                memo[string] = True
                print(memo)
                return True
    else:
        memo[string] = False
        print(memo)
        return False


# python caches the memo.
# to avoid false possitive pass an empty memo.

print(can_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd"], {})) # true
print(can_construct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk","boar"], {})) # false
print(can_construct_memo("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {})) # true
print(can_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee"
], {})) # false
