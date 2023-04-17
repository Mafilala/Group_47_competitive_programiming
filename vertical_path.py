from collections import defaultdict
import sys, threading
input = lambda: sys.stdin.readline().strip()

def main():
  tc = int(input())
  for _ in range(tc):

      n = int(input())
      parents = list(map(int, input().split()))
      boss = 0
      patriachy = defaultdict(list)
      min_n = 0
      for i in range(n):
          p = parents[i]
          if p == i + 1:
              boss = p
          else:
              patriachy[p].append(i + 1)
      exist = set()
      ans = []
      def dfs(node, subList=[]):
          if node not in exist:
            subList.append(node)
          if not patriachy[node] and subList:
              ans.append(subList.copy())
              subList.clear()
          else:
            for child in patriachy[node]:
                dfs(child, subList)

      dfs(boss)
      print(len(ans))
      for subList in ans:
          print(len(subList))
          print(*subList)
      print()

if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
