'''
Created on 2014. 9. 4.


1.1 문자열에 포함된 문자들이 전부 유일한지를 검사하는 알고리즘을 구현하라. 다른 자료구조를 사용할 수 없는 상황이다.

@author: cho
'''

#알파벳으로 이루어진 경우
def isAlphaUniqueChar(paramStr):
    
    if not paramStr.isalpha() :
        return False
    
    #Array Initialise
    checkUniqueList = [False]*26    
    
    for ch in paramStr:
        idx = ord(ch) - 97
        
        if checkUniqueList[idx] :
            return False
        else:
            checkUniqueList[idx] = True
    
    print(checkUniqueList)
        
    return True

#모든 문자열
def isUniqueCharByHash(paramStr):
    
    #HashTable의 Key-value로 검사
    chDict = {}
    
    for ch in paramStr:
        
        if ch in chDict :
            return False
        else:
            chDict.update({ch : True})
    
    print(chDict)
    
    return True

#정렬을 한 후, 앞뒤 문자열을 비교해서 검사
def isUniqueCharBySort(paramStr):
    
    soretedStr = sorted(paramStr)
    
    for i in range(len(soretedStr) - 1):
        
        if soretedStr[i] is soretedStr[i + 1]:
            return False
        
    return True

if __name__ == '__main__':
    
    input = 'asdhbqyegwq'
    
    isUnique = isAlphaUniqueChar(input)
    
    print(isUnique)
    
    input = "af2s$23@dwe"
    
    isUnique = isUniqueCharByHash(input)
    
    print(isUnique)
    
    isUnique = isUniqueCharBySort(input)
    
    print(isUnique)
    
    
    