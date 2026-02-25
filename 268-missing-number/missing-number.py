class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_len_sum = n * (n+1) // 2
        list_sum = sum(nums)
        return total_len_sum - list_sum