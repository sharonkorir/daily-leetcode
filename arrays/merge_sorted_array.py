#APPROACH
# create a loop in the range of length of nums2(n). Insert whatever is at the current index of nums2 to the same index in nums1, this pushes the other digits in nums1 to the right.
#pop the last digit in nums 1.
# sort nums1 in ascending order once loop is done

def merge(self, nums1, m, nums2, n):
    for i in range(0, n):
        nums1.insert(i, nums2[i])
        nums1.pop()
    nums1.sort()