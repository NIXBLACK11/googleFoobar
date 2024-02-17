def solution(xs):
    print(calcAns(xs))

def calcAns(xs):
    if all(x == 0 for x in xs):
        return(0)
        
    least = -2**31
    ans = 1
    for i in xs:
        if i<0:
            least = max(least, i)
            ans=ans*i
        elif i==0:
            pass
        else:
            ans = ans*i
    
    if least == ans and len(xs)==1:
        return(ans)
    if least == ans and len(xs)!=1:
        return(0)

    if ans<0:
        ans = ans/least
    return(int(ans))
