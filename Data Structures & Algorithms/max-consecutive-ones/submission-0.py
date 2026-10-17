class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0  # our counter
        storage = []  # storing consecutive records

        length = len(nums)
        last_index = len(nums) - 1

        for i in range(0, length):
            if nums[i] == 1:
                count = count + 1
                if i == (last_index):
                    storage.append(count)
            else:
                storage.append(count)
                count = 0

        # return max consecutive
        max_index = len(storage) - 1
        storage.sort()
        max_consec = storage[max_index]
        return max_consec

