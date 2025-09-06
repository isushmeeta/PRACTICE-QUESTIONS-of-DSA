#input=[0,1,3,0,2,2,4,2]
#output=5

def removeOccurence(arr, ele):
    k=0

    for i in range(len(arr)):
        if arr[i]!=ele:
            arr[k]= arr[i]
            k=k+1
    return k
arr=[0,1,3,0,2,2,4,2]
ele=2
print(removeOccurence(arr,ele))