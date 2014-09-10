'''
Created on 2014. 9. 4.

1.3 두개의 문자열이 주어졌을 때 두개가 서로의 순열인지 파악하는 메서드를 구현하라.

@author: cho
'''
#정렬 후 값을 비교
def isPermutationBySort(oneStr, anotherStr):
    
    if len(oneStr) is not len(anotherStr):
        return False
    
    sortedStr1 = sorted(oneStr)
    sortedStr2 = sorted(anotherStr)
    
    return sortedStr1 == sortedStr2
    
#문자 출현 회수로 비교
def isPermutationByCounting(oneStr, anotherStr):
    
    if len(oneStr) is not len(anotherStr):
        return False
    
    str_dict = {}
    
    for ch in oneStr:
        
        if ch in str_dict:
            str_dict.update({ch : str_dict.get(ch) + 1})
        else:
            str_dict.update({ch : 1})
    
    for ch in anotherStr:
        
        if ch in str_dict:
            
            num = str_dict.get(ch) - 1
            
            str_dict.update({ch : num})
            
            if num < 0:
                return False
        else:
            return False
        
    return True
    

if __name__ == '__main__':
    
    oneStr = "asd"
    
    anotherStr = "sdw"
    
    isPerm = isPermutationBySort(oneStr, anotherStr)
    
    print(isPerm)
    
    isPerm = isPermutationByCounting(oneStr, anotherStr)
    
    print(isPerm)
    
    