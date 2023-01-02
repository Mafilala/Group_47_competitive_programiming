class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = 0
        dd = defaultdict(int) # returns 0 for non existent key
        # dd[non existent key] returns 0 instead of raising an error
        for d in deliciousness:
            for i in range(22):
                count += dd[2 ** i - d]
                # if there is a number in a dict which,  when
                # added to the current value of d gives a power
                # of two number, our count will increase accordingly
            dd[d] += 1
        return count % 1000000007
