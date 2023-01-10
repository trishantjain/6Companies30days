'''

    --> LeetCode 150.: --Evaluate Reverse Polish Notation--

    Ques. You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
          Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:

        The valid operators are '+', '-', '*', and '/'.
        Each operand may be an integer or another expression.
        The division between two integers always truncates toward zero.
        There will not be any division by zero.
        The input represents a valid arithmetic expression in a reverse polish notation.
        The answer and all the intermediate calculations can be represented in a 32-bit integer.

'''


class Solution:
    def evalRPN(self, tokens):
        ans = []

        for i in tokens:
            try:
                ans.append(int(i))

            except:
                a = ans.pop()
                b = ans.pop()

                if (i == "+"):
                    res = a+b

                elif (i == "-"):
                    res = a-b

                elif (i == "/"):
                    res = int(a-b)

                elif (i == "*"):
                    res = a-b

                ans.append(res)

        else:
            m = ans.pop()
            return m


if __name__ == "__main__":
    Solution()
