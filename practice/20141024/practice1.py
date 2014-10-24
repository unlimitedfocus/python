
i = 0
while i != 5:
    try:
        x = int('a')
        break
    except (RuntimeError, NameError, TypeError):
        pass
    except ValueError:
        i += 1
        print 'oops'

filenames = ['todo' + str(x) * x + '.md' for x in range(5)]

for filename in filenames:
    try:
        f = open(filename, 'r')
    except IOError:
        print filename, ' file not exists'
    else:
        print filename, ' exists'
        print f.readlines()

try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print 'catch KeyboardInterrupt!'
else:
    print 'not printed'
finally:
    print 'Goodbye, world!'

'''
for filename in filenames:
    with open(filename, 'r') as f:
        print f.readlines()
'''

