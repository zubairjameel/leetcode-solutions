class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        ans = []  # will store (position, time)

        # calculate time for each car to reach target
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            ans.append((position[i], time))

        # sort by position in descending order
        ans.sort(reverse=True)

        fleet = 0
        maxtime = 0

        # iterate over cars from closest to target
        for pos, t in ans:
            if t > maxtime:
                fleet += 1
                maxtime = t
            # if t <= maxtime, car joins fleet ahead (no new fleet)

        return fleet
