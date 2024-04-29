class Solution:
    def minBitFlips(self, start: int, goal: int):
        xor = start ^ goal
        return bin(xor).count('1')

if __name__ == '__main__':
    solution = Solution()
    start = 10
    goal = 7
    print(solution.minBitFlips(10, 7))