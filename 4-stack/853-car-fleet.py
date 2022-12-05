class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort(key=lambda x: x[0], reverse=True)

        def catch(back, x):
            xend = (target - x[0])/x[1]
            backend = (target - back[0])/back[1]
            return xend <= backend

        r = []
        for x in ps:
            if len(r) == 0 or not catch(r[-1], x):
                r.append(x)
        return len(r)