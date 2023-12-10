a = [1, 2, 3]
b = a
c = a.copy()

b[0] = 5
c[1] = 6

result = (a == b, a == c, id(a) == id(b), id(a) == id(c))
print(result)