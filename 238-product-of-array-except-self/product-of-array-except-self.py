class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [-1,1,0,-3,3]
        n = len(nums)
        left = [1] * n
        right = [1] * n

        # left: [1,-1,-1,0,0]
        for i in range(n-1):
            left[i+1] = left[i] * nums[i]
        
        # right: [1,3,-9,0,0]
        for i in range(n-1):
            right[n-i-2] = right[n-i-1] * nums[n-i-1]
        
        return [right[i] * left[i] for i in range(n)]