
def f(x):
    return x % 2 != 0 and x % 3 != 0

print filter(f, range(25))

def cube(x):
    return x * x * x

def cube2(x):
    return x ** 3

print map(cube, range(25))
print map(cube2, range(25))

def add(x, y):
    return x + y

print reduce(add, range(1, 11))

def sum(l):
    def add(x, y):
        return x + y
    return reduce(add, l)

print sum(range(1, 11))

squares = []
for x in range(10):
    squares.append(x)
print squares

squares2 = [x for x in range(10)]
print squares2

result = [(x, y, z) for x in range(5) for y in range(3) for z in range(2) if x != y]
print len(result)
print result

for item in result:
    print item

ll = [[1, 2, 3], [1, 2]]
ret = [item for l in ll if len(l) != 3 for item in l if item != 2]
print ret

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

print [[row[i] for row in matrix] for i in range(4)]

print zip(*matrix)

del matrix[1:]
print matrix

t = 12, 'ab', 1.0
print t


s1 = 'hello',
s2 = 'hello'

print s1
print s2

i1 = 1, 2
print i1

x, y = i1
print x
print y


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print fruit

print 'apple'in fruit

a = set('abracadabra')
b = set('alacazam')
print 'a:', a
print 'b:', b

print '-:', a - b
print '|:', a | b
print '&:', a & b
print '^:', a ^ b

tel = {'jack': 4098, 'sape': 4139}
del tel['sape']
print tel

d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print [x for x in d]
print [d[x] for x in d]

print [d[x] for x in d if x != 'guido']

print d['guido'] not in [d[x] for x in d if x != 'guido']

for i, value in enumerate(d):
    print i, d[value]

col1 = ['no', 'name']
col2 = [1, 'jc']

for item in zip(col1, col2):
    print item

for i in reversed(range(2, 11, 2)):
    print i

for item in sorted(zip(col1, col2)):
    print item





