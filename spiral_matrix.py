class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direction = [[0,1], [1, 0], [0, -1], [-1, 0]]
        
        
        result = []
        steps = 1
        r, c = rStart, cStart
        i = 0
        while len(result)<rows*cols:
            for _ in range(2):
                delta_row, delta_column = direction[i]
                for _ in range(steps):
                    if (0 <= r < rows and 0<= c < cols):
                        result.append([r,c])
                    r, c = r + delta_row, c + delta_column
                    
                i = (i + 1)%4
            steps +=1
        
        return result