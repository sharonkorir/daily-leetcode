def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_nums = 0
        ans = []
        for i in range(len(nums)):
            sum_nums += nums[i]
            ans.append(sum_nums)
        return ans

# approach: loop through the array, at every index, add sum of numbers (sum_nums) to the value of number at current index. append the new sume of numbers to an empty array(ans)
# this approach doesn't take space and time complexity into consideration