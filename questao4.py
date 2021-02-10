def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

N = int(input("What's the array's size? "))
arr = list (map (int, input(f"Type the numbers, separated by whitespaces\n").strip().split()))[:N]
print(arr)
print("Sorted: ")
print(bubbleSort(arr))
