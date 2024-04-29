from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_nums = nums[0]
        for i in range(1, len(nums)):
            xor_nums = xor_nums ^ nums[i]
        if xor_nums == k:
            return 0
        binary =  bin(xor_nums ^ k)
        return binary.count('1')

if __name__ == '__main__':
    solution = Solution()
    nums = [2,1,3,4]
    k = 1
    print(solution.minOperations(nums, k))