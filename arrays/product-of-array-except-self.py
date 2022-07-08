#this answer fails space complexity, solution can't be submitted

#approach, loop through the array to get the value of digits before the current index (prefix) and the value of digits after (suffix) current index. Multiply prefix and suffix

def productExceptSelf(self, nums):
    answer = []
    for i in range(len(nums)):
        prefix = 1
        suffix = 1
        for j in range(0, i):
            prefix *= nums[j]
        for k in range(i+1, len(nums)):
            suffix *= nums[k]
        answer.append((prefix*suffix))
    return answer