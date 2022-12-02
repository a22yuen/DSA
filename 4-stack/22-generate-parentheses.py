from typing import List

def generateParenthesis(n: int) -> List[str]: 
        def r(ret, arr, n, s):
            if n == 0 and arr == 0:
                ret.append(s)
            else:
                if n > 0:
                    arr += 1
                    r(ret, arr, n-1, s + "(")
                if arr > 0:
                    r(ret, arr-1, n, s + ")")
        arr = 1
        ret = []
        r(ret, arr, n-1, "")
        return ret

print("hi")
print(generateParenthesis(2))