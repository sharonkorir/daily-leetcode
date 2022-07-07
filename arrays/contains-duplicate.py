def containsDuplicate(self, nums):
    my_nums = set(nums)
    if len(my_nums) == len(nums):
        return False
    else:
        return True
        
# APPROACH:
# converted the array into a set to get rid of duplicates. If the length of the set is equal to the length of the nums array then there is no duplicate therefore return false