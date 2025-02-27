# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

from itertools import combinations

class Solution(object):
    def combinationSum3(self, k, n):
        out = []
        lst = [i for i in range(1, 10)]
        comb = list(combinations(lst, k))
        for i in comb:
            temp = list(i)
            if sum(temp) == n:
                out.append(temp)
        return out

def main():
    k = int(input("Enter value of k: "))
    n = int(input("Enter value of n: "))
    sol = Solution()
    result = sol.combinationSum3(k, n)
    print("Possible combinations:", result)

if __name__ == "__main__":
    main()

