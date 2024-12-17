// Given an integer array nums and an integer val, remove all occurrences of val
// in nums in-place. The order of the elements may be changed. Then return the
// number of elements in nums which are not equal to val.

#include <stdio.h>

int removeElement(int *nums, int numsSize, int val) {
  int i, j = 0;
  for (i = 0; i < numsSize; i++) {
    if (nums[i] != val) {
      nums[j] = nums[i];
      j++;
    }
  }
  return j;
}

int main() {
  int nums[100], numsSize, val, i;

  printf("Enter the number of elements in the array: ");
  scanf("%d", &numsSize);

  printf("Enter the elements of the array:\n");
  for (i = 0; i < numsSize; i++) {
    scanf("%d", &nums[i]);
  }

  printf("Enter the value to remove: ");
  scanf("%d", &val);

  int newSize = removeElement(nums, numsSize, val);

  printf("The new size of the array is: %d\n", newSize);
  printf("The array after removing %d is:\n", val);
  for (i = 0; i < newSize; i++) {
    printf("%d ", nums[i]);
  }
  printf("\n");

  return 0;
}
