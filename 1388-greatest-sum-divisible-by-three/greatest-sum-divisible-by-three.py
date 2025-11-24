class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ss = sum(nums)
        if ss % 3 == 0:
            return ss
        
        ones = [x for x in nums if x % 3 == 1]
        twos = [x for x in nums if x % 3 == 2]
        one, two = 10e9, 10e9
        if ss % 3 == 1:
            # Remove the smallest sum with remainder 1
            # 1 ones
            if len(ones) >= 1:
                one = min(ones)
            # 2 twos
            if len(twos) >= 2:
                two = min(twos)
                twos.remove(two)
                two += min(twos)
            if one == 10e9 and two == 10e9:
                return 0
            return ss - min(one, two)
        
        else:
            if len(twos) >= 1:
                two = min(twos)
            if len(ones) >= 2:
                one = min(ones)
                ones.remove(one)
                one += min(ones)
            if one == 10e9 and two == 10e9:
                return 0
            return ss - min(one, two)