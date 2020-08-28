if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    #print(arr)
    m=max(arr)
    while m==max(arr):
        arr.remove(max(arr))
    print(max(arr))
    
