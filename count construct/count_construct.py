# return the number of ways that can construct by any combination of words

from typing import List
# unoptiomized

def count_construct(string: str, words: List[str]):
    if string=="":
        return 1
    
    count = 0
    for word in words:
        if string.startswith(word):
            cnt = count_construct(string.removeprefix(word), words)
            count += cnt
    else:
        return count



print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk","boar"])) # 0
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee"
])) # 0
