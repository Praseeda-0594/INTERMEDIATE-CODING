# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return

            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)
        return res

def main():
    digits = input("Enter digits (2-9): ")
    sol = Solution()
    result = sol.letterCombinations(digits)
    print("Possible letter combinations:", result)

if __name__ == "__main__":
    main()
