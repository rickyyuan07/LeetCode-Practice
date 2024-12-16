class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ss = set()
        for num in nums:
            if num in ss:
                return True
            ss.add(num)
        
        return False