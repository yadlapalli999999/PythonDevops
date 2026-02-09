import operator

print("All operators in the operator module:", dir(operator)) # it is a function object

print("*" * 50) # scalar multiplication

print("All operators in the operator module:", operator.__all__) # it is a object method

# All operators in the operator module: 
# ['abs', 'add', 'and_', 'attrgetter', 
# 'call', 'concat', 'contains', 'countOf', 'delitem', 'eq', 'floordiv', 
# 'ge', 'getitem', 'gt', 'iadd', 'iand', 'iconcat', 'ifloordiv', 
# 'ilshift', 'imatmul', 'imod', 'imul', 'index', 'indexOf', 'inv', 'invert',
# 'ior', 'ipow', 'irshift', 'is_', 'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le', 'length_hint',
# 'lshift', 'lt', 'matmul', 'methodcaller', 'mod', 'mul', 'ne', 'neg', 'not_', 'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub', 
# 'truediv', 'truth', 'xor']

# Arithemetic Operators
a = 10
b = 20

# first Way
print("Addition:", a + b) 
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)

print("*" * 50)
# second way
print("Addition:", operator.add(a,b))
print("Subtraction:", operator.sub(a,b))
print("Multiplication:", operator.mul(a,b))
print("Division:", operator.truediv(a,b))
print("Floor Division:", operator.floordiv(a,b))
print("*" * 50)

# comparsion operators
x= 15
y=25

#first way
print("Equal:", x==y)
print("Not Equal:", x!=y)
print("Greater than:", x>y)
print("Less than:", x < y)
print("Greater than or Equal to:", x>=y)
print("Less than or Equal to:", x<=y)

print("#" * 60)

# second way
print("Equal:", operator.eq(x,y))
print("Not Equal:", operator.ne(x,y))
print("Greater than:", operator.gt(x,y))
print("Less than :", operator.lt(x,y))
print("Greater than or Equal to:", operator.ge(x,y))
print("Less than or Equal to:", operator.le(x,y))

print("#" * 60)

# Assigment operators

# assignment Operators

m = 5
n = 10
print("\nAssignment Operators:")
# first way
print("Initial m:", m)
m += n
print("After m += n:", m)
m -= n
print("After m -= n:", m)
m *= n
print("After m *= n:", m)
m /= n
print("After m /= n:", m)
m //= n
print("After m //= n:", m)

# second way
m = 5  # Reset m
print("#" * 60)
print("Initial m:", m)
m = operator.iadd(m, n)
print("After m += n:", m)
m = operator.isub(m, n)
print("After m -= n:", m)
m = operator.imul(m, n)
print("After m *= n:", m)
m = operator.truediv(m, n)
print("After m /= n:", m)
m = operator.floordiv(m, n)
print("After m //= n:", m)


# Logical Operators

p = True
q = False

print("\nLogical Operators:")
# first way
print("AND:", p and q)
print("OR:", p or q)
print("NOT p:", not p)
print("NOT q:", not q)

print("#" * 60)
# second way
print("AND:", operator.and_(p, q))
print("OR:", operator.or_(p, q))
print("NOT p:", operator.not_(p))
print("NOT q:", operator.not_(q))


#membership Operators

list1 = [1, 2, 3, 4, 5]

print("\nMembership Operators:")

# first way
print("Is 3 in list1?:", 3 in list1)
print("Is 6 not in list1?:", 6 not in list1)
print("#" * 60)

# second way
print("Is 3 in list1?:", operator.contains(list1, 3))
print("Is 6 not in list1?:", not operator.contains(list1, 6))


# identity Operators
obj1 = [1, 2, 3]
obj2 = obj1
print("Is obj1 is obj2?:", obj1 is obj2)
print("Is obj1 is not obj2?:", obj1 is not obj2)

print("#" * 60)
print("Is obj1 is obj2?:", operator.is_(obj1, obj2))
print("Is obj1 is not obj2?:", operator.is_not(obj1, obj2))
