"""
There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mm² assuming all letters are 1mm wide.

input format:
first line=25 space-separated integers describing the height of each letter
second line=single word with lowercase letters

input:
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

output:
9
"""


def designerPdfViewer(h, word):
    heights = list(map(int, h.split()))
    m = max([heights[ord(l) - ord('a')] for l in word])

    return m * len(word)


h = input()
word = input()
print(designerPdfViewer(h, word))
