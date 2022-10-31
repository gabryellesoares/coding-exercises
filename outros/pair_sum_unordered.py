from typing import List

# assuming that the input is a descending numbers list
# i could use the function "in" to check if the complement (sum - value) is on the list
# or i could sort the list and use the same solution i was using in the other problem
# for this one i'm making a set with the complements


def find_pair(numbers: List[int], sum: int) -> bool:
    compl = set()

    for n in numbers:
        if n in compl:
            return True
        compl.add(sum - n)

    return False


print(find_pair([2, -2, 1, 2], 4))
