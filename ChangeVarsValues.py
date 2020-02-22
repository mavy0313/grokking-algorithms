# swap two vars algorithms
# with third temp var
a = 5
b = 2
print(a)
print(b)
temp = a
a = b
b = temp
print(a)
print(b)

# with 2 temp vars
a = 5
b = 2
print(a)
print(b)
tmp1 = b
tmp2 = a
a = tmp1
b = tmp2
print(a)
print(b)

# with python assignment
a = 5
b = 2
print(a)
print(b)
tmp1, tmp2 = b, a
a, b = tmp1, tmp2
print(a)
print(b)

# with python assignment
a = 5
b = 2
print(a)
print(b)
a, b = b, a
print(a)
print(b)