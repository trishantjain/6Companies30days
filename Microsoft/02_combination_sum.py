'''

    --> LeetCode 216.: --Combination Sum III--

    Ques. Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

        Only numbers 1 through 9 are used.
        Each number is used at most once.

    Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

'''


class Solution:

    def twist(self, k, su, need, done, start):
        if (k == 0 and su == need):
            return [list(done)]

        ans = []
        for i in range(start, 10):
            if (i not in done):
                if (su+i < need):
                    done.add(i)
                    ans += self.twist(k-1, su+i, need, done, i+1)
                    done.remove(i)

        return ans

    def combinationSum3(self, k, n):
        return self.twist(k, 0, n, set(), 1)
