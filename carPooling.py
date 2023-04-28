class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        print(trips)
        initialCapacity = 0
        east_dist = 0
        on_trip = []
        for trip in trips:
            initialCapacity += trip[0]
            east_dist = trip[1]
            on_trip.append(trip)
            reserve = []
            for t in on_trip:
                if t[2] <= east_dist:
                    initialCapacity -= t[0]
                else:
                    reserve.append(t)
            on_trip = reserve
            print(initialCapacity)
            if initialCapacity > capacity:
                return False
        return True
