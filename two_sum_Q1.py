# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (# both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
# LeetCode: Two Sum, Algorithm Question #1

class Solution(object):

    ## Linear search solution
    # Leetcode rank: 89.15%, time: 40ms
    # enumerate Array = [3, 5, 2, 1, 4, 7]
    # enumerate(Array)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        processed = {}
        for i in range(0, len(nums)):
            if target-nums[i] in processed:
                return [processed[target-nums[i]]+1,i+1]
            processed[nums[i]]=i

    '''
    ## Sorting and Search Solution
    # Leetcode rank: 52.58%, time: 48ms
    # enumerate Array = [3, 5, 2, 1, 4, 7]
    # enumerate(Array)
    # [(0, 3), (1, 5), (2, 2), (3, 1), (4, 4), (5, 7)]
    # lambda:
    # Defining a function to return the second element of an array of a tuple
    # g = lambda x: x(1)
    # g((0, 4)) = 4
    # sorted(array, key)
    # Here, key is to sort with the second element of a tuple in the enumerated array.
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = sorted(enumerate(nums), key=lambda x:x[1])
        i = 0; j = len(nums)-1
        while i < j:
            if L[i][1]+L[j][1] == target:
                if L[i][0] < L[j][0]:
                    return L[i][0]+1, L[j][0]+1
                else:
                    return L[j][0]+1, L[i][0]+1
            elif L[i][1]+L[j][1] > target:
                j -= 1
            else:
                i += 1
        return -1,-1
    '''

sol = Solution()

## Question Test
nums = [2, 7, 11, 15]
target = 9

index1, index2 = sol.twoSum(nums, target)
print index1, index2