##Python is easy to learn
##http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6/Intro
print "Hello, World!"

print "Jack and Jill went up a hill"
print "to fetch a pail of water;"
print "Jack fell down, and broke his crown,"
print "and Jill came tumbling after."

print "2 + 2 is", 2 + 2
print "3 * 4 is", 3 * 4
print "100 - 1 is", 100 - 1
print "(33 + 2) / 5 + 11.5 is", (33 + 2) / 5 + 11.5

print "Halt!"
#user_reply = raw_input("Who goes there? ")
#print "You may pass,", user_reply

a = 123.4
b23 = 'Spam'
first_name = "Bill"
b = 432
c = a + b
print "a + b is", c
print "first_name is", first_name
print "Sorted Parts, After Midnight or", b23

#number = input("Type in a number: ")
#text = raw_input("Type in a string: ")
#print "number =", number
#print "number is a", type(number)
##print "number * 2 =", number * 2
#print "text =", text
#print "text is a", type(text)
#print "text * 2 =", text * 2

a = 0
while a < 10:
    a = a + 1
    print a


#n = input("Number? ")
n = -10
if n < 0:
    print "The absolute value of", n, "is", -n
else:
    print "The absolute value of", n, "is", n

_ = 10
print _

number = 5
while number > 1:
    print ".",
    number = number - 1
print

def absolute_value(n):
    if n < 0:
        n = -n
    return n

a = 23
b = -23

if absolute_value(a) == absolute_value(b):
    print "The absolute values of", a, "and", b, "are equal"
else:
    print "The absolute values of", a, "and", b, "are different"

def hello():
    print 'hello'

hello()
hello()

#which_one = input("What month (1-12)? ")
which_one = 1
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

if 1 <= which_one <= 12:
    print "The month is", months[which_one - 1]


demolist = ["life", 42, "the universe", 6, "and", 9]
print "demolist = ",demolist
demolist.append("everything")
print "after 'everything' was appended demolist is now:"
print demolist
print "len(demolist) =", len(demolist)
print "demolist.index(42) =", demolist.index(42)
print "demolist[1] =", demolist[1]

# Next we will loop through the list
c = 0
while c < len(demolist):
    print "demolist[", c, "] =", demolist[c]
    c = c + 1

del demolist[2]
print "After 'the universe' was removed demolist is now:"
print demolist
if "life" in demolist:
    print "'life' was found in demolist"
else:
    print "'life' was not found in demolist"

if "amoeba" in demolist:
    print "'amoeba' was found in demolist"

if "amoeba" not in demolist:
    print "'amoeba' was not found in demolist"

demolist.sort()
print "The sorted demolist is", demolist

## This program runs a test of knowledge

# First get the test questions
# Later this will be modified to use file io.
def get_questions():
    # notice how the data is stored as a list of lists
    return [["What color is the daytime sky on a clear day? ", "blue"],
            ["What is the answer to life, the universe and everything? ", "42"],
            ["What is a three letter word for mouse trap? ", "cat"]]

# This will test a single question
# it takes a single question in
# it returns True if the user typed the correct answer, otherwise False

def check_question(question_and_answer):
    # extract the question and the answer from the list
    question = question_and_answer[0]
    answer = question_and_answer[1]
    # give the question to the user
    given_answer = raw_input(question)
    # compare the user's answer to the testers answer
    if answer == given_answer:
        print "Correct"
        return True
    else:
        print "Incorrect, correct was:", answer
        return False

# This will run through all the questions
def run_test(questions):
    if len(questions) == 0:
        print "No questions were given."
        # the return exits the function
        return
    index = 0
    right = 0
    while index < len(questions):
        # Check the question
        if check_question(questions[index]):
            right = right + 1
            index = index + 1
        # go to the next question
        else:
            index = index + 1
        # notice the order of the computation, first multiply, then divide
    print "You got", right * 100 / len(questions), \
        "% right out of", len(questions)

# now let's run the questions

run_test(get_questions())

# http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6
