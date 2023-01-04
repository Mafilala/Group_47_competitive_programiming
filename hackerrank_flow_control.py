if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if n in [2, 3, 4, 5]:
            print("Not Weird")
        elif n in [x for x in range(6, 21)]:
            print("Weird")
        else:
            print("Not Weird")
