# Remove fullstops from a string: Given a string with alphanumeric characters and fullstops, write a program to remove the fullstops from the string.

def remove_fullstops(input_string):
  return input_string.replace('.', '')

input_string = input("Enter a string with fullstops: ")
result = remove_fullstops(input_string)
print(result)

