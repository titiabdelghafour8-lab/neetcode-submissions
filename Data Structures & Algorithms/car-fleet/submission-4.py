class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        t_hours = [(target - position[i]) / speed[i] for i in range(n)]
        cars = sorted(zip(position, t_hours, range(n)), reverse=True)
        fleet_count = 1
        i = 1
        t_fleet = cars[0][1]
        while i < n:
            t_current = cars[i][1]
            if t_fleet < t_current:
                t_fleet = t_current
                fleet_count += 1
                i += 1 
                continue
            i += 1
        return fleet_count
            

                          