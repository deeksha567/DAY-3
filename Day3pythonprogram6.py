#NON REPRESENTABLE INTEGER

def Smallest(arr,n):
    sum = 1
    for i in range(0, n):
        if arr[i] <= sum:
            sum = sum + arr[i]
        else:
            break
    return sum


n1 = int(input("Enter number of elements in list: "))
arr1 = []
print("Enter elements of list: ")
for i in range(n1):
    c = int(input())
    arr1.append(c)
arr1.sort()
print("Smallest non-representable number: ", Smallest(arr1, n1))
