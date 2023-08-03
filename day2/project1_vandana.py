list_a=input("Enter a number")
num_list=list_a.split(",")
for i in num_list:
    i=i.lstrip()
    i=i.rstrip()
    div=[]
    for j in range(2,10):
        if j==2:
            if int(i[-1]) in [0,2,4,6,8]:
                div.append(j)
        
        if j==3:
            k=i
            if int(i) < 0:
                k=abs(int(i))
                k=str(k)
                sum_nums=0
                for q in range(len(k)):
                    sum_nums+=int(k[q])

                if int(int(sum_nums)/3)*3==int(sum_nums):
                    div.append(j)
        if j==9:
            k=i
            if int(i) < 0:
                k=abs(int(i))
                k=str(k)
                sum_nums=0
                for q in range(len(k)):
                    sum_nums+=int(k[q])

                if int(int(sum_nums)/9)*9==int(sum_nums):
                    div.append(j)
        if j==8:
            k=i
            if int(i) < 0:
                k=abs(int(i)) 
                k=str(k)
            while len(k)>1:
                k=(int(k[:-1])*2)+int(k[-1])
                k=str(k)
            if int(k)==8 or int(k)==0:
                div.append(j)
        if j==7:
            k=i
            if int(i) < 0:
                k=abs(int(i))
                k=str(k)
            while len(k)>1:
                k=int(k[:-1])+(int(k[-1]))*5
                k=str(k)
            if int(k)==7 or int(k)==0:
                div.append(j)
        
        if j==5:
            l_d=i[-1]
            if int(l_d)==0 or int(l_d)==5:
                div.append(j)
        if j==4:
            if len(i) > 1:
                if int(i[-2]) in [0,2,4,6,8]:
                    if int(i[-1]) in [0,4,8]:
                        div.append(j)
            
                elif int(i[-2]) in [1,3,5,7,9]:
                    if int(i[-1]) in [2,6]:
                        div.append(j)
            else:
                if int(i[-1]) in [0,4,8]:
                    div.append(j)
        if j==6:
            if 2 in div and 3 in div:
                div.append(j)
    print(div)
