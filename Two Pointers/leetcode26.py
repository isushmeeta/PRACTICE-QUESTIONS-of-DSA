#leetcode26
#remove duplicates
class Solution:
    def removeDuplicates(self, nums):
      if not nums:
         return 0

      k=1
      for i in range(1,len(nums)):
         if nums[i]!= nums[k-1]:
          nums[k]= nums[i]
          k+=1
      
      return k,nums[:k]

nums = [1, 1, 2]
solution = Solution()
length, new_nums = solution.removeDuplicates(nums)
print("Length:", length)
print("Array without duplicates:", new_nums)


























#the below code logically okay but uses extra space not acceptable

# arr=[1,1,2]

# uniq=[]
# seen=set()


# for i in arr:
#     if i not in seen:
#         uniq.append(i)
#         seen.add(i)

# k=len(uniq)

# print(k,",",uniq)