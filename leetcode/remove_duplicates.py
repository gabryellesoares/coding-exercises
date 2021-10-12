from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    j = 0
    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            nums[k] = nums[i]
            k += 1
            j += 1

    return k
