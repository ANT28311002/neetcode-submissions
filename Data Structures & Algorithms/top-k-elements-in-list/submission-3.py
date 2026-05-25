class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_copy = nums[:]
        result = []
        for j in range (0,k):
           max_count = 0
           max_num = None
           for num in set(nums_copy):
                count = nums_copy.count(num)
                if count>max_count:
                    max_count = count
                    max_num = num
            
                max1 = max_num
           result.append(max1)

           nums_copy = [n for n in nums_copy if n != max_num]

        return result

        
       