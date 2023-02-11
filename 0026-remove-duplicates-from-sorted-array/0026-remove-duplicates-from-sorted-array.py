class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        
        prev = 0
        for current in range(1,len(nums)):
            if nums[current]!=nums[prev]:
                prev+=1
                nums[prev]=nums[current]

        return prev+1
        # count = 0
        # for i in range(len(nums)):
        #     if i < len(nums) - 2 and nums[i] == nums[i + 1]:
        #         continue
        #     nums[count] = nums[i]
        #     count += 1
        # return count