from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Recursively run down each option of either adding ) or (, keeping track of both numbers
        # use backtracking by adding and removing what you added after each recursive call to reuse stack and save time
        # global return array to save time.
        ret = []

        def r(cl, op, s):
            # no more (), return
            if op == 0:
                s.append(')' * cl)
                ret.append("".join(s))
                s.pop()
            else:
                # still some open
                s.append("(")
                r(cl+1, op-1, s)
                s.pop()
                if cl > 0:
                    s.append(")")
                    r(cl-1, op, s)
                    s.pop()
        cl = 0
        op = n
        st = []
        r(cl, op, st)
        return ret
