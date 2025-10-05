class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        ans = 0
        for i in range(1, n-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                peak = i
                # find the left slope
                left = peak
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1

                # find the right slope
                right = peak
                while right < n-1 and arr[right+1] < arr[right]:
                    right += 1
                
                cur = right - left + 1
                ans = max(ans, cur)
        
        return ans
