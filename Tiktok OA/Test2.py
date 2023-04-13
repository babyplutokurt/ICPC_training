class Solution:
    def canPartition(self, nums) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s = s // 2
        dp =[True] + [False] * s
        for num in nums:
            for j in range(s + 1):
                if dp[j] and j + num < s + 1:
                    dp[j + num] = True

        print(dp)
        return dp[s]

a = Solution()
a.canPartition([1,2,5])