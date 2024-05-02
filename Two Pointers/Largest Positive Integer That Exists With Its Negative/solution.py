from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        max_k = float('-inf')
        i, j = 0, len(nums) - 1
        while i < j:
            _sum = nums[i] + nums[j]
            if _sum == 0:
                max_k = max(max_k, nums[j])
                j -= 1
                i += 1
            elif _sum > 0:
                j -= 1
            else:
                i += 1
        if max_k != float('-inf'):
            return max_k
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,2,-3,3]
    print(solution.findMaxK(nums))
    
# Time complexity - O(nlogn)
# Space complexity - O(1) without sorting O(n) if sorting is considered