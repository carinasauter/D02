#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:

def do_twice(x):
    return x + x

def do_four(x):
    return do_twice(x) + do_twice(x)

def limit():
    return ('+ ' + do_four('- '))

def inner():
    return('| ' + do_four('  '))

def row(o,i):
    return (o + '\n' +
            4 * (i + '\n'))

def two_by_two():
    
    outer_lines = do_twice(limit()) + '+'
    inner_lines = do_twice(inner()) +'|'
    print(do_twice(row(outer_lines, inner_lines)), end='')
    print (outer_lines)

    


def four_by_four():
    outer_lines = do_four(limit()) + '+'
    inner_lines = do_four(inner()) +'|'
    print(do_four(row(outer_lines, inner_lines)), end='')
    print (outer_lines)










# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    two_by_two()
    four_by_four()
    



if __name__ == "__main__":
    main()
