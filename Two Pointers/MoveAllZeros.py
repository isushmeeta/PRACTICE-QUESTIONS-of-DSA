#Move all zeros
def Moveallzeros(arr):
    count=0 #for non zero elements

    for i in range (len(arr)):
        if arr[i]!=0:
            arr[i],arr[count]=arr[count], arr[i]
            count+=1
    return arr
arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(Moveallzeros(arr))
#time O(n), space o(1)            