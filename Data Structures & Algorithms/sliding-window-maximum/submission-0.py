class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        #两个情况排除之后，剩下的队首就是每个段里最大的
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
             
            left = r - k + 1

            if q[0] < left:
                q.popleft()
            
            if left >= 0:
                output.append(nums[q[0]])

        return output