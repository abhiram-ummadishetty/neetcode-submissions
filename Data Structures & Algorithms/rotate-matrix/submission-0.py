class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        left,right = 0, n-1
        
        while left<right:
            for i in range(right-left):
                top,bottom = left,right
                #save the top left value
                temp = matrix[top][left+i]
                #move the bottom left to the top left
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = temp
            left+=1
            right-=1
            
        print(matrix)
                
    
             


        