#!/usr/bin/python

# Define isPalindrome() function
def isPalindrome(string):
    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

# Define main() function
def main():
    string = input("Enter a string: ")
    if isPalindrome(string):
        print(string + " is a palindrome")
    else:
        print(string + " is not a palindrome")

# Execute functions
main()
