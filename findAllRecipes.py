class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for i in range(len(recipes)):
            recipe = recipes[i]
            for ing in ingredients[i]:
                graph[ing].append(recipe)
                incoming[recipe] += 1
        print(graph)
        # print(incoming)
        queue = deque()
        
        for val in recipes + supplies:
            if incoming[val] == 0:
                queue.append(val)

        
        possibles = set()
        print(queue)
        while queue:
            pop = queue.popleft()
            if pop in recipes:
                possibles.add(pop)
            if pop in supplies or pop in recipes:
                for rec in graph[pop]:
                    incoming[rec] -= 1
                    if incoming[rec] == 0:
                        queue.append(rec)
        return possibles
