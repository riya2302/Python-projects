class Solution():
    def searchMatrix(self, matrix, target):
        flag = 0
        for x in range(rows):
            for y in range(coloumn):
                if(matrix[x][y]==target):
                    flag = 1
                    break
                else:
                    continue
        if(flag==1):
            return bool(1)
        else:
            return bool()
            
a1 = Solution()
matrix = []
rows = int(input("Enter the number of rows: "))
coloumn = int(input("Enter the number of coloums: "))

print("Enter the matrix entries rowwise:")
for x in range(rows):
    a = []
    for y in range(coloumn):
        data = int(input())
        a.append(data)
    matrix.append(a)   

print("Entered matrix is: ")    
for x in range(rows):
    for y in range(coloumn):
        print(matrix[x][y],end=' ')
    print()
    
    
target = int(input("Enter the target: "))
print(a1.searchMatrix(matrix,target))
