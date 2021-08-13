def f1(n):
    li=[]
    summ=0
    x=1
    count=0
    while summ+x<=n:
        summ+=x
        x*=2
        count+=1
    return count
    
def f2(n):
    x=0
    y=1 
    li=[]
    summ=0
    while True:
        z=x+y 
        x=y 
        y=z
        li.append(y)
        if summ+z>=n:
            break
        summ+=z
    return len(li)
        
        
        
def solution(total_lambs):
        n = total_lambs
        return f2(n)-f1(n)
    
print(solution(143))
