# http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6
onetoten = range(1, 11)
for count in onetoten:
    print count

for count in range(1, 11):
    print count

demolist = ['life', 42, 'the universe', 6, 'and', 9, 'everything']
for item in demolist:
    print "The Current item is:",
    print item

list = [2, 4, 6, 8]
sum = 0
for num in list:
    sum += num

print "The sum is:", sum

list = [4, 5, 7, 8, 9, 1, 0, 7, 10]
list.sort()
prev = list[0]
del list[0]
for item in list:
    if prev == item:
        print "Duplicate of", prev, "found"
    prev = item

a = 6
b = 7
c = 42
print 1, a == 6
print 2, a == 7
print 3, a == 6 and b == 7
print 4, a == 7 and b == 7
print 5, not a == 7 and b == 7
print 6, a == 7 or b == 7
print 7, a == 7 or b == 6
print 8, not (a == 7 and b == 6)
print 9, not a == 7 and b == 6

list = ["Life", "The Universe", "Everything", "Jack", "Jill", "Life", "Jill"]

# make a copy of the list. See the More on Lists chapter to explain what [:] means.
copy = list[:]
# sort the copy
copy.sort()
prev = copy[0]
del copy[0]

count = 0

# go through the list searching for a match
while count < len(copy) and copy[count] != prev:
    prev = copy[count]
    count = count + 1

# If a match was not found then count can't be < len
# since the while loop continues while count is < len
# and no match is found

if count < len(copy):
    print "First Match:", prev

## This programs asks a user for a name and a password.
# It then checks them to make sure the user is allowed in.

#name = raw_input("What is your name? ")
name = 'Josh'
#password = raw_input("What is the password? ")
password = 'Friday'
if name == "Josh" and password == "Friday":
    print "Welcome Josh"
elif name == "Fred" and password == "Rock":
    print "Welcome Fred"
else:
    print "I don't know you."
