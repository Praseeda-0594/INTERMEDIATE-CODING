// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    int k = 0; 
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] != nums[i + 1]) {
            nums[k++] = nums[i];
        }
    }
    nums[k++] = nums[numsSize - 1]; 
    return k;
}

int main() {
    int nums[100], numsSize, i;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &numsSize);

    printf("Enter the sorted elements of the array:\n");
    for (i = 0; i < numsSize; i++) {
        scanf("%d", &nums[i]);
    }

    int newSize = removeDuplicates(nums, numsSize);

    printf("The new size of the array is: %d\n", newSize);
    printf("The array after removing duplicates is:\n");
    for (i = 0; i < newSize; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");

    return 0;
}
