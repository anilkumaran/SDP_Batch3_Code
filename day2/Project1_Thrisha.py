list1=input().split(',')
for i in list1:
    list2 = []
    for j in range(2,10):
        if j == 2 and int(i[-1]) in [0,2,4,6,8]:
            list2.append(j)
        if j == 3 or j == 9:
            sum = 0
            z = 1
            if int(i)<0:
                z=int(i)*-1
            else:
                z=i
            for k in str(z):
                sum = sum+int(k)
            if (int(int(sum)/j))*j==int(sum):
                list2.append(j)
        if j == 4:
            k=i
            if int(i)<0:
                k=int(i)*-1
                k=str(k)
            if len(k)>1:
                if int(k[-2]) in [0,2,4,6,8]:
                    if int(k[-1]) in [0,4,8]:
                        list2.append(j)
                elif int(k[-2]) not in [0,2,4,6,8]:
                    if int(k[-1]) in [2,6]:
                        list2.append(j)
            else:
                if int(k[-1]) in [0,4,8]:
                    list2.append(j)
        if j == 5:
            r = i[::-1]
            if int(r[0])==5 or int(r[0])==0:
                list2.append(j)
        if j == 6:
            if 2 in list2 and 3 in list2:
                list2.append(j)
        if j == 7:
            k = i
            if int(i)<0:
                k=int(i)*-1
                k=str(k)
            while len(k)>1:
                k=(int(k[:-1]))+(int(k[-1])*5)
                k=str(k)
                if int(k) == 7 or int(k)==0:
                    list2.append(j)
        if j == 8:
            k=i
            if int(i)<0:
                k=int(i)*-1
                k=str(k)
            while len(k)>1:
                k=(int(k[:-1])*2)+int(k[-1])
                k=str(k)
            if int(k)==8 or int(k)==0:
                list2.append(j)
    s = ''
    for k in list2:
        s+=str(k)
        s+=','
    if(len(list2)==0):
        print(i+": is not divisible")
    else:
        print(i+": divisible by "+s[:-1])
