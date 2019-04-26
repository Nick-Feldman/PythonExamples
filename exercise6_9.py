#Please write a program which prints all permutations of [1,2,3]
from itertools import permutations

perm = permutations([1,2,3])


print(len(list(perm)))
