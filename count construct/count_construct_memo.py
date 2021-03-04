# return the number of ways that can construct by any combination of words

from typing import List
# optiomized

def count_construct_memo(string: str, words: List[str], memo={}):
    if string in memo:
        return memo[string]

    if string=="":
        return 1
    
    count = 0
    for word in words:
        if string.startswith(word):
            cnt = count_construct_memo(string.removeprefix(word), words, memo)
            count += cnt
    else:
        memo[string] = count
        return count


# Unlike js, python caches the memo.
# So we should put empty memo to avoid false possitives.

print(count_construct_memo("purple", ["purp", "p", "ur", "le", "purpl"], {})) # 2
print(count_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd"], {})) # 1
print(count_construct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk","boar"], {})) # 0
print(count_construct_memo("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {})) # 4
print(count_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee"
], {})) # 0
