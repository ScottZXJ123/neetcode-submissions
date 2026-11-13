class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        sums = {0}
        for num in nums:
            newsum = set(sums)
            for s in sums:
                newsum.add(num + s)
            sums = newsum
        return target in sums