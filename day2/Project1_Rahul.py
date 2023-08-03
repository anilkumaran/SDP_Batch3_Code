
strngg = input("Enter the numbers : \n")

arr = strngg.split(",")

for i in range(0,len(arr)):
    arr2 = []
    x = arr[i]
    #By 2--------
    if(x[-1] in ('2','4','6','8','0')):
        arr2.append(2)
    #By3-----
    sum = 0
    for j in range(0,len(x)):
        sum = sum + int(x[j])
    while(sum > 9):
        strng = str(sum)
        sum = 0
        for i in range(0,len(strng)):
            sum = sum + int(strng[i])
    if(sum in (3,6,9,0)):
        arr2.append(3)
    #BY4------
    if(len(x)>1):
        if(x[-2] in ('2','4','6','8','0') and x[-1] in ('0','4','8')):
            arr2.append(4)
        elif(x[-2] in ('3','1','5','7','9') and x[-1] in ('2','6')):
            arr2.append(4)
    elif(x[-1] in ('4','8')):
        arr2.append(4)
    #By5--------
    if(x[-1] in ('0','5')):
        arr2.append(5)
    #BY6--------
    if((2 in arr2) and (3 in arr2)):
        arr2.append(6)
    #By7---------
    z = 7
    k = 1
    while(z * k <= int(x)):
        if(z * k == int(x)):
            arr2.append(7)
            break
        k = k + 1
    #BY8-------
    var = int(x[-3:])
    for i in range(0,var+1,8):
        if(i==int(x)):
            arr2.append(8)

    #BY9-----
    sume = 0
    for j in range(0,len(x)):
        sume = sume + int(x[j])
    while(sume > 9):
        stro = str(sume)
        sume = 0
        for i in range(0,len(stro)):
            sume = sume + int(stro[i])
    if(sume == 9):
        arr2.append(9)
    if(len(arr2) == 0):
        print("{} : is not divisible ".format(int(x)))
    else:
        s = ""
        for ele in arr2:
            s = s + str(ele) + ","
        s = s[:-1]
        print("{} :is divisible by {} ".format(int(x),s))
 

    
    


        
    
        
    
