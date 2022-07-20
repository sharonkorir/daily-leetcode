# APPROACH:
#set value of number at index zero to initial current_sum and initial maximum_sub_array.
#loop through array, and for every number, the new maximum_sub_array will be the greater of the two(current number, and current number + current max_sub array).
#update the new current sum with the greater of the two( new maximum_sub_array, and current sum)

def maxSubArray(nums):
    current_sum = nums[0]
    max_sub_arr = nums[0]

    for i in range(1, len(nums)):
        max_sub_arr = max(nums[i], nums[i] + max_sub_arr)
        current_sum = max(current_sum, max_sub_arr)
    
    return current_sum