class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        seen=[]
        ans=[]   
        for i in range(len(nums)):
            if seen and seen[0] == i-k:
                seen.pop(0)

            while seen and nums[seen[-1]] < nums[i]:
                seen.pop()

            seen.append(i)
            if i >= k-1:
                ans.append(nums[seen[0]])
        return ans                