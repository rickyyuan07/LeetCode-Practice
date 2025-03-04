class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        dd = {} # element -> next larger element, hashmap for mapping the answers for nums2
        stack = [] # (index, element), this stores the position that have not found their "next larger element"

        for i in range(n):
            # Every time the current element is larger than some elements in the monotonic stack,
            # that means we found an answer for the element with the index
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
