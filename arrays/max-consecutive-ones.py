#APPROACH
# loop through an array counting the 1s, for every 1, increment the count by 1. Every time you run into a zero, reset the count to 0. return the maximum count value.

def findMaxConsecutiveOnes(self, nums):
    count = 0
    answer = 0
    for i in range(0,len(nums)):
        
        if nums[i] == 0:
            """reset the count to 0 every time you run into a 0"""
            count = 0
        else:
            """the count will record each time a 1 was encountered, and reset on encountering a 0. maximum consecutive ones will be the maximum value of the counter"""
            count +=1
            #print(count)
            answer = max(answer, count)
    return answer
