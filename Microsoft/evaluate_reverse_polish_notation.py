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
