'''
Faraday School of Mathematics
Carol Pan and Leo Liu
SoftDev2 pd 7
K #16: Ready, Set, Math!
2018-04-26
'''


def union(a, b):
    return a + [x for x in b if not x in a]

def intersection(a, b):
    return [x for x in b if x in a]

def set_difference(a, b):
    return [x for x in a if not x in b]

def sym_difference(a, b):
    return set_difference(a,b) + set_difference(b,a)

def cart_product(a, b):
    return [(x,y) for x in a for y in b]

a = [0,1,2,3]
b = [0,2,4,6]

print union(a,b)
print intersection(a,b)
print set_difference(a,b)
print sym_difference(a,b)
print cart_product(a,b)
