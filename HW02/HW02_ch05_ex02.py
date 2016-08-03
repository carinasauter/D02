#!/usr/bin/env python
# HW02_ch05_ex02

# Fermat's Last Theorem says that there are no positive integers a, b, and c 
# such that 
#        a^n + b^n = c^n 
# for any values of n greater than 2.

# (1) Write a function named check_fermat that takes four parameters-a, b, c and 
# n-and that checks to see if Fermat's theorem holds. If n is greater than 2 
# and it turns out to be true that
#        a^n + b^n = c^n 
# the program should print, "Holy smokes, Fermat was wrong!"" 
# Otherwise the program should print, "No, that doesn't work."

# (2) Write a function named check_fermat_ints that prompts the user to input 
# values for a, b, c and n, converts them to integers, and uses check_fermat
# to check whether they violate Fermat's theorem.

################################################################################
# Write your functions below:
def check_fermat(a, b, c, n):
    if n>2 and a**n + b**n == c**n:
        print( "Holy smokes, Fermat was wrong!")
    else:
        print( "No, that doesn't work.")


def check_fermat_ints():
    text = input("So you want to test Fermat's Theory? Please provide values for a,b,c,n (in that order, separated by commas, no spaces) to test the famous formula \n a^n + b^n = c^n \n")
    a=int(text[0])
    b=int(text[2])
    c=int(text[4])
    n=int(text[6])
    check_fermat(a, b, c, n)


# Write your functions above:
################################################################################
def main():
    """Call your function within this function.
    When complete have one function call in this function:
    check_fermat_ints()
    and two functions defined in the body:
    check_fermat_ints()
    check_fermat()
    """
    check_fermat_ints()



if __name__ == "__main__":
    main()
