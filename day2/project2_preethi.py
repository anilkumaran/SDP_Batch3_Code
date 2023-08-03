n=input("enter the number")
l=n.split(",")
for i in l:
    s=[]
    i=i.rstrip()
    i=i.lstrip()
    a=int(i[-1])
    for j in range(2,10):
        
        if j==2 :
            if int(i[-1]) in[0,2,4,6,8]:
                s.append(j)
        if j==5:
            if int(i[-1]) in [0,5]:
                s.append(j)
        if j==3 :
            k=i
            if int(i)<0:
                k=abs(int(i))
                k=str(k)
                sum=0
                for q in range(len(k)):
                    sum+=int(k[q])
                if int(int(sum)/3)*3==int(sum):
                    s.append(j)

        if j==9:
            k=i
            if int(i)<0:
                k=abs(int(i))
                k=str(k)
                sum=0
                for q in range(len(k)):
                    sum+=int(k[q])

                if int(int(sum)/9)*9==int(sum):
                     s.append(j)
        if j==8:
            k=i
            if int(i)<0:
                k=abs(int(i))
                k=str(k)
            while len(k)>1:
                k=(int(k[:-1])*2)+int(k[-1])
                k=str(k)
            if int(k)==8 or int(k)==0:
                s.append(j)
        if j==7:
            k=i
            if int(i)<0:
                k=abs(int(i))
                k=str(k)
            while len(k)>1:
                k=int(k[:-1])+(int(k[-1]))*5
                k=str(k)
            if int(k)==0 or int(k)==7:
                s.append(j)
        if j==4:
            if len(i)>1:
                if int(i[-2]) in [0,2,4,6,8]:
                    if int(i[-1]) in [0,4,8]:
                        s.append(j)
                elif int(i[-2]) in [1,3,5,7,9]:
                    if int(i[-1]) in [2,6]:
                        s.append(j)
            else:
                if int(i[-1]) in[0,4,8]:
                    s.append(j)
        if j==6:
            if 2 in s and 3 in s:
                s.append(j)

    print(s)
