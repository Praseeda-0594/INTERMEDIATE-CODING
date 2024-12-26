# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution(object):
  def moveZeroes(self, nums):
      nums1 = []
      nums2 = []
      for i in nums:
          if i == 0:
              nums2.append(i)
          else:
              nums1.append(i)
      nums[:] = nums1 + nums2
      return nums

if __name__ == "__main__":
  solution = Solution()
  input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
  result = solution.moveZeroes(input_list)
  print("Modified List:", result)
