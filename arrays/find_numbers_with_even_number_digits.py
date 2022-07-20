#Approach:
#loop through nums, convert current number too string then find its length. if length modulus 2 is zero, increment the even number count

def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_numbers = 0
        for i in range(0, len(nums)):
            if (len(str(nums[i])) % 2) == 0:
                even_numbers += 1
        return even_numbers