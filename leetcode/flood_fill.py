from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    if image[sr][sc] == newColor:
        return image

    return helper(image, sr, sc, len(image), len(image[0]), newColor, image[sr][sc])


def helper(image: List[List[int]], sr: int, sc: int, m: int, n: int, newColor: int, oldColor: int) -> List[List[int]]:
    if sr < 0 or sc < 0 or sr >= m or sc >= n or image[sr][sc] != oldColor:
        return

    image[sr][sc] = newColor
    helper(image, sr+1, sc, m, n, newColor, oldColor)
    helper(image, sr-1, sc, m, n, newColor, oldColor)
    helper(image, sr, sc+1, m, n, newColor, oldColor)
    helper(image, sr, sc-1, m, n, newColor, oldColor)

    return image
