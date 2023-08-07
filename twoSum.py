#two number sum in a list
class Solution:
    def twoSum(self,nums,target):
        a = []
        for j in range(size):
            for k in range(j+1,size):
                if(nums[j]+nums[k]==target):
                    a.append(j)
                    a.append(k)
                    break
                else:
                    continue
        return a
     
a1=Solution()
nums = []
size = int(input("Enter the size: "))
      
    
for i in range(size):
    data = int(input("Enter the items: "))
    nums.append(data)
print("Entered list: ",nums)
    
target = int(input("Enter the target: "))
print("Indices are: ",a1.twoSum(nums,target))
