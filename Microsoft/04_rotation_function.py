'''

    --> LeetCode 396.: --Rotate Function--

    Ques. You are given an integer array nums of length n.

        Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

            F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].

            Return the maximum value of F(0), F(1), ..., F(n-1).

        The test cases are generated so that the answer fits in a 32-bit integer.

'''

import collections

class Solution:
    def maxRotateFunction(self, nums):
        list_sum = []  # This list stores sum of elements of rotating list
        nums_len = len(nums)  # Length of original list

        rotate_deque = collections.deque(nums)

        for _ in range(nums_len):
            # Rotate original list every time by 1 position
            rotate_deque.rotate(1)
            rotate_list = list(rotate_deque)

            # Sum of elements multiplying by its index after rotating
            f = 0
            for j in range(nums_len):
                f += j*rotate_list[j]

            list_sum.append(f)

        return max(list_sum)
