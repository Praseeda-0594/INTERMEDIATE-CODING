#Given an input string s, reverse the order of the words. The words in s will be separated by at least one space. Return a string of the words in reverse order concatenated by a single space.

class Solution(object):
  def reverseWords(self, s):
      w = s.split()
      r = ' '.join(reversed(w))
      return r

if __name__ == "__main__":
  solution = Solution()
  input_string = input("Enter a string: ")
  result = solution.reverseWords(input_string)
  print("Original String:", input_string)
  print("Reversed Words:", result)
