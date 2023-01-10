'''

    --> LeetCode 391.: --Perfect Rectangle--

    Ques. Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is  (xi, yi) and the top-right point of it is (ai, bi).

        Return true if all the rectangles together form an exact cover of a rectangular region.

'''


class Solution:
    def isRectangleCover(self, rectangles):
        corners = set()
        area = 0

        for rec in rectangles:
            bottom_left = (rec[0], rec[1])
            top_right = (rec[2], rec[3])
            top_left = (rec[0], rec[3])
            bottom_right = (rec[2], rec[1])

            area += (rec[2] - rec[0])*(rec[3]-rec[1])

            for i in [bottom_left, top_right, top_left, bottom_right]:
                if i not in corners:
                    corners.add(i)

                else:
                    corners.remove(i)
        
        if len(corners) != 4:
            return False

        corners = sorted(corners)
        first = corners.pop(0)
        last = corners.pop()

        wholeArea = (last[0] - first[1]) * (last[0] - first[1])

        return area == wholeArea


p = Solution()
print(p.isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [
                   3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]))
