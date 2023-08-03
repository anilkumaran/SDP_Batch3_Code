list=input().split(",")
val=0
for i in list:
    try:
        if int(i) or int(i)==0:
            val=1
            continue
    except:
        print("Enter integer value in place of "+i)
        val=0
if val==1:
    for i in list:
        i=i.lstrip()
        i=i.rstrip()
        div_list=[]
        for j in range(2,10):
            if j==2 and int(i[-1]) in [0,2,4,6,8]:
                div_list.append(j)
            if j==3 or j==9:
                sum=0
                z=1
                if int(i)<0:
                    z=int(i)*-1
                else:
                    z=i
                for k in str(z):
                    sum=sum+int(k)
                if (int(int(sum)/j))*j==int(sum):
                    div_list.append(j)
            if j==4:
                k=i
                if int(i)<0:
                    k=int(i)*-1
                    k=str(k)
                if len(k)>1:
                    if int(k[-2]) in [0,2,4,6,8] :
                        if int(k[-1]) in [0,4,8]:
                            div_list.append(j)
                    elif int(k[-2]) not in [0,2,4,6,8]:
                        if int(k[-1]) in [2,6]:
                            div_list.append(j)
                else:
                    if int(k[-1]) in [0,4,8]:
                        div_list.append(j)
            if j==5:
                if int(i[-1])==5 or int(i[-1])==0:
                    div_list.append(j)
            if j==6:
                if 2 in div_list and 3 in div_list:
                    div_list.append(j)
            if j==7:
                k=i
                if int(i)<0:
                    k=int(i)*-1
                    k=str(k)
                while len(k)>1:
                    k=(int(k[:-1]))+int(k[-1])*5
                    k=str(k)
                if int(k)==7 or int(k)==0:
                    div_list.append(j)
            if j==8:
                k=i
                if int(i)<0:
                    k=int(i)*-1
                    k=str(k)
                while len(k)>1:
                    k=(int(k[:-1])*2)+(int(k[-1]))
                    k=str(k)
                if int(k)==8 or int(k)==0:
                    div_list.append(j)
        s=''
        for k in div_list:
            s+=str(k)
            s+=','
        if(len(div_list)==0):
            print(i+":is not divisible")
        else:
            print(i+"is divisible by "+s[:-1])
            
