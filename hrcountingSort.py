def countingSort(arr):
    # Write your code here
    arr2 = [0] * 100
    for i in arr:
        arr2[i] += 1
    return arr2
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
