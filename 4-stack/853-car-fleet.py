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

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(list(zip(position, speed)), reverse=True)
        time, r = 0, 0
        for pos, spe in ps:
            t = (target-pos)/spe
            if t > time:
                time = t
                r += 1
        return r