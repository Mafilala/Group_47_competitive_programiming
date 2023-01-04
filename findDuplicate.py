class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash_map = {}
        ans = []
        for path in paths:
            main = path.split()[0]
            files = path.split()[1:]
            store = []
            for file in files:
                idx = file.index("(")
                content = file[idx + 1: -1]
                if content not in hash_map.keys() and content: # if content is not empty and also not in hash_map
                    new_list = list()
                    new_list.append(main + "/" + file[: idx])
                    hash_map[content] = new_list
                else:
                    hash_map[content].append(main + "/" + file[: idx])
        ans = [v for v in hash_map.values() if len(v) > 1]
        return ans
