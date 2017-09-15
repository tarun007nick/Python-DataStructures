#Program to check whether the two strings are anagram or not

#Method to check the anagram status of two strings.

def anagram(s1,s2):
    
    alist = list(s2)
    pos1 = 0
    stillOK = True
    
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
                
        if found:
            alist[pos2] = None
            print("The 2nd list is ",alist)
        else:
            stillOK = False
            
        pos1 = pos1+1
        
    return stillOK 
             
#Pass the two strings to the anagram function
print(anagram("abcdef", "fedbac"))