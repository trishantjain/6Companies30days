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
