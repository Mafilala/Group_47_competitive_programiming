class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill) - 1
        ans = []
        target = skill[i] + skill[j]
        while i < j:
            if skill[i] + skill[j] == target:
                ans.append(skill[i] * skill[j])
                i += 1
                j -= 1
            else:
                return -1
        return sum(ans)
