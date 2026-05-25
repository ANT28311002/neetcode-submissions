class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        for i in range(n):
            product = 1
            if i == 0:
                for j in range(1,n):
                    product *= nums[j]
        
            elif i == n-1:
                for j in range(0,n-1):
                    product*=nums[j]
                
            
            else: 
                for j in range(0,i):
                    product*=nums[j]
                for j in range(i+1,n):
                    product*=nums[j]
        
            output.append(product)

        return output