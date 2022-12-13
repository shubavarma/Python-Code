# Creating a module to accept a string and perform string operations with out using any string methods
def upper(str):
    s=""
    for y in str:
        if ord(y) in range(65,91):
            s+=y
        elif ord(y) in range(97,123):
            s+=(chr(ord(y)-32))
        else:
            s+=y
    return s     

def lower(str):
    s=""
    for y in str:
        if ord(y) in range(65,91):
            s+=(chr(ord(y)+32))
        elif ord(y) in range(97,123):
            s+=y
        else:
            s+=y
    return s     

def isUpper(str):
    l=[]
    for y in str:
        if ord(y) in range(65,123):  
            if ord(y) in range(65,97):
                l.append(True)
            else:
                l.append(False)
        else:
            l.append(True)
    if len(set(l))>1:
        return False
    else:
        for y in set(l):
            if y!=False:
                return True
            else:
                return False
            
def isLower(str):
    l=[]
    for y in str:
        if ord(y) in range(65,123):
            if ord(y) in range(97,123):
                l.append(True)
            else:
                l.append(False)
        else:
            l.append(True)
    if len(set(l))>1:
        return False
    else:
        for y in set(l):
            if y!=False:
                return True
            else:
                return False       

def isAlpha(str):
    l=[]
    for y in str:
        if ord(y) in range(65,123):
            if ord(y) in range(91,96):
                l.append(False)
            else:     
                l.append(True)
        else:
            l.append(False)
    if len(set(l))>1:
        return False
    else:
        for y in set(l):
            if y!=False:
                return True
            else:
                return False         
            
def isDigit(str):
    l=[]
    for y in str:
        if ord(y) in range(48,58):
            l.append(True)
        else:
            l.append(False)
    if len(set(l))>1:
        return False
    else:
        for y in set(l):
            if y!=False:
                return True
            else:
                return False     
            
def isAlNum(str):
    l=[]
    for y in str:
        if ord(y) in range(48,123):
            if ord(y) in range(91,96):
                l.append(False)
            elif ord(y) in range(58,65):
                l.append(False)
            else:     
                l.append(True)
        else:
            l.append(False)
    if len(set(l))>1:
        return False
    else:
        for y in set(l):
            if y!=False:
                return True
            else:
                return False 
            
def swapcase(str):
    s=""
    for y in str:
        if ord(y) in range(65,91): 
            s+=(chr(ord(y)+32))
        elif ord(y) in range(97,123):
            s+=(chr(ord(y)-32))
        else:
            s+=y
    return s    

def capitalize(str):
    s=""
    for y in range(len(str)):
        if y==0:
            s+=upper(str[0]) 
        elif ord(str[y-1])==32:
            s+=upper(str[y])
        else:
            s+=str[y]
    return s

def split(str,sep):
    l=[]
    start=0
    for y in range(len(str)):
        if str[y]==sep:
            l.append(str[start:y])
            start=y+1
        elif y==len(str)-1:
            l.append(str[start:])
    return l        
            
def join(list,sep):
    s=""
    for y in list:
        s+=y+sep
    return str(s)            

def title(str):
    str1=lower(str)
    l=split(str1," ")
    l1=[]
    l2=[]
    l3=[]
    count=0
    for y in l:
        l1=list(y)
        for i in range(len(y)):
            if isAlpha(l1[i]):
                l1[i]=chr(ord(l1[i])-32)
                break
        l2="".join(l1)
        l3.append(l2)

    return join(l3," ")


def isTitle(str):
    l=split(str," ")
    l1=[]
    l2=[]
    for y in l:
        l1=list(y)
        for i in range(len(l1)):
            if isAlpha(l1[i]):
                if isUpper(l1[i]):
                    l2.append(True)
                    break
                    
                else:
                    l2.append(False)
            else:
                l2.append(True)
    if len(set(l2))==1:
        return True
    else:
        return False