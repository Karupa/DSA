word1=str(input())
word2=str(input())
w1=list(word1)
w2=list(word2)
l1=len(w1)
l2=len(w2)
print(w1,w2)
l=l2
if(l1>=l2):
     l=l1
   

def merge(a,b):
    s=''
    for i in range(l):
        try:
            s=s+w1[i]+w2[i]
        except(IndexError):
            if(len(w1)<len(w2)):
                s=s+w2[i] 
            elif(len(w1)>len(w2)):
                s=s+w1[i]
            else:
                pass
        finally:
            pass
    print(s)    

merge(w1,w2)