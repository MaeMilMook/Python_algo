'''
Created on 2014. 9. 24.

1.7 M*N 행렬의 한 원소가 0일 경우, 해당 원소가 속한 행과 열의 모든 원소를 0으로 설정하는 알고리즘을 작성하라.

@author: cho
'''

def __makeZeroCrossMatrix(matrix):
    
    zeroRIdx = -1
    zeroCIdx = -1 
    
    for ridx, row in enumerate(matrix):
        for cidx, col in enumerate(row):
            
            if col == 0:
                zeroRIdx = ridx
                zeroCIdx = cidx
                
                break
    
    
    for ridx, row in enumerate(matrix):
        for cidx, col in enumerate(row):
            
            if cidx == zeroCIdx:
                row[cidx] = 0
            
            if ridx == zeroRIdx:
                row[cidx] = 0
                 


if __name__ == '__main__':
    
    matrix = [[7, 9, 9, 2], [8, 9, 4, 9], [8, 0, 8, 2], [8, 4, 4, 2]]

    for row in matrix:
        print(row)
        
    
    __makeZeroCrossMatrix(matrix)
    
    print('==>')
    
    
    for row in matrix:
        print(row)