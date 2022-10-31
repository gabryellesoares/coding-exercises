# given 2 arrays create a function that lets a user knoe whether these 2 contain any common items

from typing import List


def contains_common(list1: List[int], list2: List[int]) -> bool:
    return len(set(list1 + list2)) != len(list1 + list2)


print(contains_common(['a', 'b', 'c', 'x'], ['z', 'y']))
