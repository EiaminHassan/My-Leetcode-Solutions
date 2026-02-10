# function to merge two halves of an array
def merge(arr, left, mid, right):
    n1 = mid-left+1
    n2 = right - mid

    # create temp arrays
    L = [0]*n1
    R = [0]*n2

    # copy data to temp arrays
    for i in range(n1):
        L[i] = arr[left+i]
    for j in range(n2):
        R[j] = arr[mid+1+j]

    # print("L: ", L)
    # print("R: ", R)

    # merge the temp arrays back into arr
    i = j = 0
    k = left
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1

    # copy the remaining elements of L, if any
    while i<n1:
        arr[k] = L[i]
        i+=1
        k+=1

    # copy the remaining elements of R, if any
    while j<n2:
        arr[k] = R[j]
        j+=1
        k+=1


# function that implements merge sort
def mergeSort(arr, left, right):
    if left<right:
        mid = (left+right)//2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,mid,right)



# driver code to test the above
if __name__ == '__main__':
    arr = [1,5,9,2,6,8,3,4,7]
    mergeSort(arr, 0, len(arr)-1)
    print(arr)