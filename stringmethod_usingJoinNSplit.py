# Creating a module to accept a string and perform string operations with out using string methods but using join and split
def upper(str):
    l=[]
    for y in str:
        if ord(y) in range(65,91):
            l.append(y)
        elif ord(y) in range(97,123):
            l.append(chr(ord(y)-32))
        else:
            l.append(y)
    return "".join(l)
            
def lower(str):
    l=[]
    for y in str:
        if ord(y) in range(65,91):
            l.append(chr(ord(y)+32))
        elif ord(y) in range(97,123):
            l.append(y)
        else:
            l.append(y)
    return "".join(l)

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
    l=[]
    for y in str:
        if ord(y) in range(65,91): 
            l.append(chr(ord(y)+32))
        elif ord(y) in range(97,123):
            l.append(chr(ord(y)-32))
        else:
            l.append(y)
    return "".join(l)            
            
def capitalize(str):
    l=str.split(" ")
    l1=[]
    l2=[]
    for y in l:
        l1=list(y)
        if ord(l1[0]) in range(97,123):
            l1[0]=chr(ord(l1[0])-32)
            l1="".join(l1)
            l2.append(l1)
        else:
            l2.append(y)
    return " ".join(l2)

def title(str):
    str1=lower(str)
    l=str1.split(" ")
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

    return " ".join(l3)  

def isTitle(str):
    l=str.split(" ")
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