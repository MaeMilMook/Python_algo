'''
Created on 2014. 9. 6.

@author: cho

1.6 이미지를 표현하는 n*n행렬이 있다. 이미지의 각 픽셀은 4byte로 표현된다.
이미지를 90도 회존시키는 메서드를 작성하라. 부가적인 행렬을 사용하지 않고서도 할 수 있는가?

'''

#Fail, 문제 인식 실패
def __turn90Matrix(matrix):
    
    for ridx, row in enumerate(matrix):
        for cidx ,col in enumerate(row):
            
            if ridx is not cidx and ridx < cidx:
                matrix[cidx][ridx], matrix[ridx][cidx] = col, matrix[cidx][ridx]                 
    


def __turn90MatrixBylayer(matrix):
    
    mtxLen = len(matrix)

    for i in range(mtxLen//2):
        
        p = mtxLen - i - 1
            
        for j in range(0, p - i):
            
            tmp = matrix[i][j + i]
            
            matrix[i][j + i] = matrix[p - j][i]
            
            matrix[p - j][i] = matrix[p][p - j]
            
            matrix[p][p - j] = matrix[j + i][p]
            
            matrix[j + i][p] = tmp
            

if __name__ == '__main__':
    
    n = 4
    
    #matrix = [[col for col in range(n)] for row in range(n)]
    #matrix = [[7, 9, 9, 2], [3, 9, 4, 9], [6, 0, 1, 2], [8, 4, 5, 2]]
    matrix = [[7, 9, 2], [3, 9, 4], [6, 0, 1]]
    #matrix = [[7, 9], [3, 4]]

    for row in matrix:
        print(row)
        
    
    __turn90MatrixBylayer(matrix)
    
    print('==>')
    
    
    for row in matrix:
        print(row)
