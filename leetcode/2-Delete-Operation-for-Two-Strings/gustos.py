"""
    19. 07. 04(Time Limit Exceeded)
    풀이: 대충 품.BRUTE FORCE문제를 뽑았어야 헀는데 DP문제를 뽑은 듯 하여 대충 풀고 나중에 개선하는걸로(LCS 응용 문제)
"""

import itertools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        tmp = word2
        if len(word1) < len(word2):
            tmp = word1

        for i in range(len(tmp), -1, -1):
            w_list1 = list(map(''.join, itertools.combinations(word1, i)))
            w_list2 = list(map(''.join, itertools.combinations(word2, i)))
            for w in w_list1:
                if w in w_list2:
                    return (len(word1) - len(w)) + (len(word2) - len(w))

        return 0
