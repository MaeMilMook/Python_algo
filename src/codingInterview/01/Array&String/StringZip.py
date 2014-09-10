'''
Created on 2014. 9. 6.

1.5 같은 문자가 연속으로 반복될 경우, 그 횟루를 사용해 문자열을 압축하는 메서드 구현

@author: cho
'''



def zipStringArray(inputStr):
    
    zipLen = __checkMaxLen(inputStr)
    
    if zipLen > len(inputStr):
        return inputStr
    
    curCh = ''
    
    cnt = 0
    
    result = []
    
    for ch in inputStr:

        if curCh == '':
            curCh = ch
        
        if curCh == ch:
            cnt = cnt + 1
        else :
            
            result.append(curCh)
            result.append(str(cnt))
            
            cnt = 1
            curCh = ch
            
    result.append(curCh)
    result.append(str(cnt))
    
    if len(inputStr) < len(result) :
        return inputStr
    else:
        return ''.join(result)
    

def __checkMaxLen(inputStr):
    
    zipLen = 0
    
    curCh = ''
    numCnt = 0
    
    for ch in inputStr:
        
        if curCh == '':
            curCh = ch
            
        if curCh == ch:
            numCnt = numCnt + 1
            
        else :
            curCh = ch
            zipLen = zipLen + len(str(numCnt)) + 1
            numCnt = 1
    
    zipLen = zipLen + len(str(numCnt)) + 1
    
    return zipLen

            
if __name__ == '__main__':
    
    string = "aaabbccccccddddeeeeeeeff"
    
    result = zipStringArray(string)
    
    print(result)
    
    
    