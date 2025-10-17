class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # m <= n
        m, n = len(nums1), len(nums2)

        total_left = (m+n+1) // 2
        left, right = 0, m

        # Binary Search on nums1
        while left <= right:
            i = (left+right) // 2  # Take i number of items for nums1
            j = total_left - i  # Take j number of items for nums2

            nums1_left_max = float('-inf') if i == 0 else nums1[i-1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j-1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if (m + n) % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    m1 = max(nums1_left_max, nums2_left_max)
                    m2 = min(nums1_right_min, nums2_right_min)
                    return (m1+m2) / 2.0
            

            if nums1_left_max > nums2_right_min:
                right = i-1
            else:
                left = i+1