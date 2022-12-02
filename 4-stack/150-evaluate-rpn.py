import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = set(["+", "-", "/", "*"])
        for x in tokens:
            if x in ops:
                op2 = str(nums.pop())
                op1 = str(nums.pop())
                val = eval("" + op1 + x + op2)
                val = math.floor(val) if val > 0 else math.ceil(val)
                nums.append(val)
            else:
                nums.append(x)
        return nums[0]