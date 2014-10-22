
x = 10

if x < 0:
    print 'neg'
elif x == 0:
    print 'zero'
else:
    print x

words = ['window', 'linux', 'osx']
for word in words[:]:
    if word == 'window':
        word = 'windows'
    print word

print range(10)
print range(1, 10, 2)

def fibo(n):
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a + b
    print ''
    # return b

fibo(2000)
#print fibo(2000)

f = fibo
f(100)

if 1 in (1, 2, 3):
    print '1 is in (1, 2, 3)'

def f(a, L=[]):
    L.append(a)
    return L

print f(1)
print f(1, [2])

def make_inc(n):
    return lambda x: x + n

f = make_inc(11)
print f(1)
print f(11)

def outer(x):
    some = 1
    def inner(y):
        return y + x + some
    return inner

f = outer(1)
print f(2)



