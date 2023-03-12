class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        li = [[p, s] for p, s in zip(position, speed)]
        li.sort()
        driver_pos, driver_spe = li.pop()
        driver_time = (target - driver_pos) / driver_spe
        fleet_count = 1
        while li:
            cur_pos, cur_spe = li.pop()
            cur_time = (target - cur_pos) / cur_spe
            if cur_time > driver_time:
                driver_time = cur_time
                fleet_count += 1
        return fleet_count
