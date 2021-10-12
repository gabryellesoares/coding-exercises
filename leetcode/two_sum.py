from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    s = {}

    for i in range(len(nums)):
        s[nums[i]] = i

    for i in range(len(nums)):
        n = nums[i] - target
        if n in s and s[n] != i:
            return [i, s[n]]
