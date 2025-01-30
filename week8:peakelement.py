# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

class Solution(object):
  def findPeakElement(self, nums):
      n = len(nums)     
      if n == 1:
          return 0       
      if n == 2:
          return 0 if nums[0] > nums[1] else 1     
      for i in range(n):
          if (i == 0 and nums[i] > nums[i+1]) or \
             (i == n-1 and nums[i] > nums[i-1]) or \
             (0 < i < n-1 and nums[i] > nums[i-1] and nums[i] > nums[i+1]):
              return i  

if __name__ == "__main__":
  nums = list(map(int, input("Enter space-separated integers: ").split()))
  solution = Solution()
  peak_index = solution.findPeakElement(nums)
  print(f"Peak element index: {peak_index}")
