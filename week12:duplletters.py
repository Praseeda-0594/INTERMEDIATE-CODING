# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

class Solution(object):
  def removeDuplicateLetters(self, s):
      stack = []
      seen = set()
      last_occurrence = {}

      for i in range(len(s)):
          last_occurrence[s[i]] = i

      for i, ch in enumerate(s):
          if ch in seen:
              continue

          while stack and stack[-1] > ch and last_occurrence[stack[-1]] > i:
              removed_char = stack.pop()
              seen.remove(removed_char)

          seen.add(ch)
          stack.append(ch)

      return ''.join(stack)

# Main function to take user input
if __name__ == "__main__":
  s = input("Enter the string: ")
  sol = Solution()
  result = sol.removeDuplicateLetters(s)
  print("Result:", result)
