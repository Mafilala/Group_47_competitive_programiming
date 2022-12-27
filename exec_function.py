if __name__ == '__main__':
    N = int(input())
    li = []
    for _ in range(N):
        command = input().split()
        if command[0] == "print":
            print(li)
        else:
            args = ",".join(command[1:])
            do = f"li.{command[0]}({args})"
            exec(do)
