# http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6
import calendar

#year = input("Type in the year number: ")
year = 2004
calendar.prcal(year)

from calendar import prcal

#year = input("Type in the year number: ")
year = 2014
prcal(year)


from time import time, ctime

prev_time = ""
#while True:
the_time = ctime(time())
if prev_time != the_time:
    print "The time is:", ctime(time())
    prev_time = the_time


def shout(string):
    for character in string:
        print "Gimme a " + character
        print "'" + character + "'"
shout("Lose")

def middle(string):
    print "The middle character is:", string[len(string) / 2]

middle("abcdefg")
middle("The Python Programming Language")
middle("Atlanta")

def to_upper(string):
    ## Converts a string to upper case
    upper_case = ""
    for character in string:
        if 'a' <= character <= 'z':
            location = ord(character) - ord('a')
            new_ascii = location + ord('A')
            character = chr(new_ascii)
        upper_case = upper_case + character
    return upper_case

print to_upper("This is Text")


# Write a file
out_file = open("test.txt", "w")
out_file.write("This Text is going to out file\nLook at it and see!")
out_file.close()

# Read a file
in_file = open("test.txt", "r")
text = in_file.read()
in_file.close()

print text

"""
def print_numbers(numbers):
    print "Telephone Numbers:"
    for x in numbers.keys():
        print "Name:", x, "\tNumber:", numbers[x]
    print

def add_number(numbers, name, number):
    numbers[name] = number

def lookup_number(numbers, name):
    if name in numbers:
        return "The number is " + numbers[name]
    else:
        return name + " was not found"

def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
    else:
        print name," was not found"

def load_numbers(numbers, filename):
    in_file = open(filename, "r")
    for in_line in in_file:
        in_line = in_line.rstrip('\n') #Eliminate end of line or enter
        name, number = in_line.split(",")
        numbers[name] = number
    in_file.close()

def save_numbers(numbers, filename):
    out_file = open(filename, "w")
    for x in numbers.keys():
        out_file.write(x + "," + numbers[x] + "\n")
    out_file.close()

def print_menu():
    print '1. Print Phone Numbers'
    print '2. Add a Phone Number'
    print '3. Remove a Phone Number'
    print '4. Lookup a Phone Number'
    print '5. Load numbers'
    print '6. Save numbers'
    print '7. Quit'
    print

phone_list = {}
menu_choice = 0
print_menu()
while True:
    menu_choice = input("Type in a number (1-7): ")
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print "Add Name and Number"
        name = raw_input("Name: ")
        phone = raw_input("Number: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        print "Remove Name and Number"
        name = raw_input("Name: ")
        remove_number(phone_list, name)
    elif menu_choice == 4:
        print "Lookup Number"
        name = raw_input("Name: ")
        print lookup_number(phone_list, name)
    elif menu_choice == 5:
        filename = raw_input("Filename to load: ")
        load_numbers(phone_list, filename)
    elif menu_choice == 6:
        filename = raw_input("Filename to save: ")
        save_numbers(phone_list, filename)
    elif menu_choice == 7:
        break
    else:
        print_menu()

print "Goodbye"
"""


def main():
    try:
        #number = int(input("Please enter a number.\n"))
        number = '2'
        half = number/2
        print "Half of the number you entered is ",half
    except NameError:
        print "NameError."
    except ValueError:
        print "ValueError."
    except SyntaxError:
        print "SyntaxError."
    except TypeError:
        print "TypeError."
    finally:
        print "I am executing the finally clause."

main()


# TODO: https://docs.python.org/2/tutorial/
# TODO: http://learnpythonthehardway.org/book/
# TODO: http://en.wikibooks.org/wiki/Python_Programming