# Is substring: Given two strings str1 and str2, write a program to return true if str2 is a substring of str1 and false otherwise.

s = input("Enter a string: ")
sub = input("Enter a substring: ")
if sub in s:
    print("True, Substring found!")
else:
    print("False, Substring not found.")
  
