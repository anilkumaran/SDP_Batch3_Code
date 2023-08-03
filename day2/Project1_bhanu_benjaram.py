n = input()
l = n.split(',')
for i in l:
    if int(i)<0:
        i=i[1:]
    #2
    l1=[]
    l2=[0,2,4,6,8]
    if int(i[-1]) in l2:
        l1.append(2)

    #3
    m=i
    sum=0
    l3=[0,3,6,9]
    while len(m)>1:
        for j in m:
            sum+=int(j)
        m=str(sum)
        sum=0
    if int(m) in l3:
        l1.append(3)
    
    #4
    f=int(i[-2:])
    if f in list(range(0,f+1,4)):
        l1.append(4)
    
    #5
    k=int(i[-1:])    
    if(k==0 or k==5):
        l1.append(5)

    #6
    if((2 in l1) and (3 in l1)):
       l1.append(6)

    # 7
    b=i
    r=1
    while(len(b)>2):
        x = int(b[-1])
        b=b[:-1]
        r=int(b)-(2*x)
        b=str(r)
    if r in list(range(0,r+1,7)):
        l1.append(7)
    
    #8
    z=int(i[-3:])
    if z in list(range(0,z+1,8)):
        l1.append(8)

    #9
    if(m=="0" or m=="9"):
        l1.append(9)

    #result
    
    if l1:
        print(i +": is divisible by")
        print(l1)
    else:
        print(i +": is not divisible")

