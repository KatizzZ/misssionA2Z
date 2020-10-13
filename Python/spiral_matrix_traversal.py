import copy
class Solution:
    lst = []
    def printMatrix(self,matrix):
        if len(matrix)<=0:
            return
        self.lst.extend(matrix[0])
        matrix.pop(0)
        for i,row in enumerate(matrix):
            if i!=len(matrix)-1:
                self.lst.append(row[len(row)-1])
                row.pop(len(row)-1)
        if len(matrix):
            self.lst.extend(matrix[len(matrix)-1][::-1])
            matrix.pop(len(matrix)-1)
        for i,row in enumerate(matrix[::-1]):
            if len(row):
                self.lst.append(row[0])
                row.pop(0)
        # matrix.pop(0)
        # if(len(matrix)):
        #     matrix.pop(len(matrix)-1)
        # for i,row in enumerate(matrix):
        #     row.pop(0)
        #     if(len(row)):
        #         row.pop(len(row)-1)
            
    def spiralOrder(self, matrix):
        self.lst = []
        column, row = len(matrix[0]),len(matrix)
        while row>0 and column>0:
            self.printMatrix(matrix)
            if len(matrix)>0:
                column, row = len(matrix[0]),len(matrix)
            else:
                break
        return self.lst
        
            

if __name__ == "__main__":
    cl = Solution()
    print(cl.spiralOrder([[1],[2],[3],[4]]))