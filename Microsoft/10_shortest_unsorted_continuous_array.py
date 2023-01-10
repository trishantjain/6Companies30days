'''

    --> LeetCode 581.: --Shortest Unsorted Continuous Subarray--

    Ques. Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

    Return the shortest such subarray and output its length.

'''


class Solution:
    def findUnsortedSubarray(self, N):
        lenN, left, right = len(N) - 1, -1, -1
        maxN, minN = N[0], N[lenN]

        for i in range(1, len(N)):
            a, b = N[i], N[lenN - i]
            if a < maxN:
                right = i
            else:
                maxN = a

            if b > minN:
                left = i
            else:
                minN = b

        return max(0, left+right-lenN+1)
