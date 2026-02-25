class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotations = k % n
        for _ in range(rotations):
            nums_last = nums.pop()
            nums.insert(0,nums_last)
        return nums