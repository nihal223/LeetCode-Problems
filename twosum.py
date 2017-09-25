class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            searchElement = target - nums[i]
            numPopped = nums.pop(i)
            for j in range(len(nums)):
                if searchElement == nums[j]:
                    nums.insert(i, numPopped)
                    #res.extend([i,nums.index(searchElement)])
                    res.extend([i, j+1])
                    return res
            nums.insert(i,numPopped)

nums = input()
target = input()

myObject = Solution();
result = myObject.twoSum(nums, target)
print result

