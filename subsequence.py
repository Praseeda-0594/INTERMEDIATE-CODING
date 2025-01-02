# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

class Solution(object):
  def isSubsequence(self, s, t):

      i, j = 0, 0
      while i < len(s) and j < len(t):
          if s[i] == t[j]:
              i = i + 1
          j = j + 1
      return i == len(s)

def main():

  solution = Solution()

  s = input("Enter the string s (subsequence to check): ").strip()
  t = input("Enter the string t (main string): ").strip()

  result = solution.isSubsequence(s, t)
  print(f"Is '{s}' a subsequence of '{t}'? {'Yes' if result else 'No'}")

if __name__ == "__main__":
  main()
