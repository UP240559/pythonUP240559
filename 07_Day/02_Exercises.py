#1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
union = A.union(B)
print(union)
#2
intersection = A.intersection(B)
print(intersection)
#3
is_subset = A.issubset(B)
print(is_subset)
#4
are_disjoint = A.isdisjoint(B)
print(are_disjoint)
#5
union_ab = A.union(B)
union_ba = B.union(A)
print(union_ab)
#6
symmetric_difference = A.symmetric_difference(B)
print(symmetric_difference)
#7
del A
del B
