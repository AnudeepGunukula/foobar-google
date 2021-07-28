def Solution(data,n):
    li=set(data)
    for i in li:
        dcount=data.count(i)
        if dcount>n:
            for j in range(dcount):
                data.remove(i)
    return data

data=[1,2,2,2,3,3,3,4,5,5,3]
n=1
print(Solution(data,n))
