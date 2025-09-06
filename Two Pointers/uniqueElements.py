#keep unique elements or remove duplicates
def uniqueElements(arr):
    count=1
    for i in range (1,len(arr)):
        if arr[i]!=arr[i-1]:
            arr[count]=arr[i]
            count=count+1
    return arr[:count]

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(uniqueElements(arr))

#time O(n) , space o(1)