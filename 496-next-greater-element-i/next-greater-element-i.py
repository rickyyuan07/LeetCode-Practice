class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        dd = {} # element -> next larger element
        stack = [] # (index, element)

        for i in range(n):
            while stack != [] and stack[-1][1] < nums2[i]:
                index, element = stack.pop()
                dd[nums2[index]] = nums2[i]
            
            stack.append((i, nums2[i]))
        
        m = len(nums1)
        ans = [-1] * m
        for i in range(m):
            if nums1[i] in dd:
                ans[i] = dd[nums1[i]]

        return ans
