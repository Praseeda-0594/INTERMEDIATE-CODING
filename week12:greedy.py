# Given two integers x and y, return any string str such that str has length x + y and contains exactly x 'x' letters, and exactly y 'y' letters.  In addition, str should not contain 'xxx' or 'yyy'. By using Greedy Approach.

def create_string(x, y):
  result = []

  while x > 0 or y > 0:
      if x > y:  # If more 'x' are left, prioritize 'xx'
          if x >= 2:
              result.append("xx")
              x -= 2
          else:
              result.append("x")
              x -= 1
      elif y > x:  # If more 'y' are left, prioritize 'yy'
          if y >= 2:
              result.append("yy")
              y -= 2
          else:
              result.append("y")
              y -= 1
      else:  # If equal, alternate
          result.append("x")
          x -= 1
          if y > 0:
              result.append("y")
              y -= 1

  return "".join(result)

# Taking user input
x = int(input("Enter the number of 'x': "))
y = int(input("Enter the number of 'y': "))

# Generating and printing the string
print("Generated String:", create_string(x, y))
