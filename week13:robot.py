# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time. Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
      dp = [[1] * n for _ in range(m)]  # Initialize grid with 1s

      for i in range(1, m):
          for j in range(1, n):
              dp[i][j] = dp[i-1][j] + dp[i][j-1]

      return dp[m-1][n-1]

def main():
  m = int(input("Enter number of rows: "))
  n = int(input("Enter number of columns: "))
  solution = Solution()
  result = solution.uniquePaths(m, n)
  print("Number of unique paths:", result)

if __name__ == "__main__":
  main()
