arr=[5,6,7,12,9]
#max
max_val=arr[0]
for i in arr:
    if i>max_val:
        max_val=i

#min
minVal=arr[0]
for i in arr:
    if i< minVal:
        minval=i

print(max_val)
print(minVal)

#total

total=0
for i in arr:
    total+=i
print (total)
#reverse
left, right= 0, len(arr)-1
while left < right:
    arr[left],arr[right]=arr[right], arr[left]
    left+=1
    right-= 1
print(arr)

k=2
n=len(arr)
k%=n

arr=arr[-k:]+arr[:-k]
print(arr)#12,9,5,6,7

#remove duplicates
arr2=[5,6,7,7,12,9]
uniq=[]
seen=set()
for i in arr2:
    if i not in seen:
        uniq.append(i)
        seen.add(i)
print(uniq)

#counting frequencies 
#Logic: Use a dictionary (or Python’s collections.Counter)

frq={}
for i in arr2:
    frq[i] = frq.get(i, 0) + 1
print(frq)