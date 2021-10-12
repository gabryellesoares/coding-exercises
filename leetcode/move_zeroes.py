from typing import List


def moveZeroes(nums: List[int]) -> None:
    is_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[is_zero] = nums[is_zero], nums[i]
            is_zero += 1
