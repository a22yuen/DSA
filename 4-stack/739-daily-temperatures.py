class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We want to keep track of all days we've come across, and eventually compare them with each current element to see if the current element is warmer
        # On each temperature, we will compare it to the temperatures before
        # If it is greater, then pop the old date and continue
        # If it is less than or equal to, add to stack as it is not warmer.
        # Following this pattern with each temperature will create a monotonically decreasing stack, ensuring we only need to check the top of the stack for validity
        stack = []
        ret = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while len(stack) > 0 and t > temperatures[stack[-1]]:
                s = stack.pop()
                ret[s] = i-s
            stack.append(i)
        return ret
            