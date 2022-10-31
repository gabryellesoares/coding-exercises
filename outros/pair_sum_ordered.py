from typing import List

# assuming that the input is a ascending numbers list


def find_pair(numbers: List[int], sum: int) -> bool:
    i = 0
    j = len(numbers) - 1

    while i != j:
        if (numbers[i] + numbers[j] == sum):
            return True
        if (numbers[i] + numbers[j] > sum):
            j -= 1
        else:
            i += 1

    return False


print(find_pair([1, 2, 3], 3))
