"""
Permutations of "ABC" is as below,
ABC
ACB
BAC
BCA
CAB
CBA

"""

def permutation(text, mutation=''):
    if len(text) == 0:
        print(mutation)
    else:
        for i in range(len(text)):
            newmutation = mutation + text[i]
            newtext = text[0:i] + text[i+1:]
            permutation(newtext, newmutation)

tex = "ABC"
permutation(tex)