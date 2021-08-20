def solution(xs):
    ans=0
    arr=sorted(xs)
    pos,neg=[],[]
    for i in arr:
        if i>0:
            pos.append(i)
        elif i<0:
            neg.append(i)
    if len(neg)%2!=0:
        if len(neg)!=1:
             neg=neg[:-1]
        elif len(neg)==1 and len(pos)==0:
            if 0 in xs:
                return str(0)
            return str(neg[0])
        elif len(neg)==1 and len(pos)!=0:
            neg=[]
    pos+=neg
    count=0
    for i in pos:
        if count==0:
            ans=1
        ans*=i
        count+=1
    ans=str(ans)
    return ans

if __name__=="__main__":
    arr=[2,-2,-3,5]
    print(solution(arr))