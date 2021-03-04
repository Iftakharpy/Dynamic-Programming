# return if the string can be coonstructed by any combination of words

from typing import List
# unoptiomized

def can_construct(string: str, words: List[str]):
    if string=="":
        return True

    for word in words:
        if string.startswith(word):
            if can_construct(string.removeprefix(word), words):
                return True
    else:
        return False




print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # true
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk","boar"])) # false
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # true
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee"
])) # false