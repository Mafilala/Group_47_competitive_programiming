class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        reference = defaultdict(int)
        for cpd in cpdomains:
            num, dom = cpd.split()
            num = int(num)
            num_of_dot = dom.count(".")
            for _ in range(num_of_dot):
                new_num = num
                new_num += reference[dom]
                reference[dom] = new_num
                index = dom.index(".")
                dom = dom[index + 1:]
            new_num = num
            new_num += reference[dom]
            reference[dom] = new_num
        ans = [f"{value} {key}" for key, value in reference.items()]
        return ans
