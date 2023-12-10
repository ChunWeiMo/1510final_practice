import copy

a = [1, [2, 3], (4, 5, [6, 7])]
b = a[:]
c = copy.copy(a)
d = copy.deepcopy(a)

a[1][1] = 10
a[2][2][0] = 11

print(f'a == b, a == c, a == b: {a == b, a == c, a == b}')
print(f'a == d: {a == d}')
print(f'a is b: {a is b}')
