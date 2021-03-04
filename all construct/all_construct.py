# return if the string can be coonstructed by any combination of words
from pprint import pp
from typing import List
# unoptiomized

def all_construct(string: str, words: List[str]):
    if string=="":
        return [[]]
    
    constructs = []
    for word in words:
        if string.startswith(word):
            construct = all_construct(string.removeprefix(word), words)
            if len(construct)>0:
                constructs.extend([[word, *x] for x in construct])
    else:
        return constructs
# O(n^m + n*m)


pp(all_construct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
pp(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
pp(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk","boar"])) # 0
pp(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
pp(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee"
])) # 0
