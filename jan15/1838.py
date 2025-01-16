from types import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        l = 0
        totalSum = 0
        res = -1 

        for r in range(len(nums)):
            totalSum += nums[r]
            windowLength = r - l + 1
            if windowLength * nums[r] > totalSum + k:
                totalSum -= nums[l]
                l += 1
                continue
            res = max(res, windowLength)
        return res

# Time Complexity: O(nlogn + n) = O(nlogn), where n is the length of nums
# Sort nums takes nlogn time, and doing the sliding window takes n time

# Space Complexity: O(1), we only use a few extra variables, and no extra data structures to store anything

# Solution:
# So I am thinking we can first sort the array, and then find a optimal sub window of nums that contains the maxFrequency of numbers after we use all of our k operations
# I am thinking, we can keep expanding the sub window, until we reach a point where k can longer increment all the values in the sub window to 
# be equal to the largest value in that subwindow.
# And because we sorted before, we can get the largest value in our subwindow really easily by just 
# looking at the last element in the subwindow, which will just be nums[r]
# And we can check if k is not enough by multiping the largest value in our subwindow(nums[r]) by the length of the window, 
# effectively giving us the number that totalSum + k should surpass or equal
# If it does not, we know we need to shrink the window, and we can do that by incrementing l, and subtracting nums[l] from totalSum
# We continue this process until we reach the end of the array, and we keep track of the max window length we have seen so far,
#  as that represents the frequency of our subwindow if k is enough, and return that as the answer