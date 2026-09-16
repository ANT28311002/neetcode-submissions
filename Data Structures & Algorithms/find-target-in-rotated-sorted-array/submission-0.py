class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            val = nums.index(target)
            return val
        else:
            return -1