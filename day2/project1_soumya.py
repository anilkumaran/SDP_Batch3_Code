nums = input("Enter nums : ")
nums = nums.split(',')

#---------------------------
def sum_of_digits(a):
    sum = 0
    for i in a:
        sum += int(i)
    if(sum > 9):
        sum = sum_of_digits(str(sum))
    return sum

def check_div_seven(n):
    by_seven_num = n
    while(len(by_seven_num) > 2):
        by_seven_num =str( int(by_seven_num[-1])*5 + int(by_seven_num[:-1]))
    return int(by_seven_num)

def check_div_eight(n):

    by_eight = n
    while(len(by_eight) > 2):
        by_eight = str( int(by_eight[:-1]) * 2 + int(by_eight[-1]))
        #print("eight.....")
    return int(by_eight)

def is_even(n):
    if(n ^ 1 == n+1):
        return 1 
    elif(n^1 == n-1):
        return 0
    
def check_div_four(n):
    res = 0
    if(len(n) == 1 and n in ['4','8']):
        res = 1
    else:
        if (is_even(int(n[-2])) == 1 and int(n[-1]) in [0,4,8] )or(is_even(int(n[-2]))== 0 and int(n[-1]) in [2,6]):
            res = 1  
    return res  
   


#---------------------------
#main implementation
for n in nums:
    
    divis = []  
    is_divis_by_2 = False
    is_divis_by_3 = False

    #by2
    if(n[-1] in ['0','2','4','6','8']):
       divis.append(2)
       is_divis_by_2 = True
    #by3
    if(sum_of_digits(n) in [3,6,9]):
        divis.append(3)
        is_divis_by_3 = True   
    #by4
    if(check_div_four(n) == 1):
        divis.append(4)     

    #by5   
    if(n[-1] in ['5','0']):
       divis.append(5)             
     
    #by6
    if(is_divis_by_3 and is_divis_by_2):
        divis.append(6)
    #by7
    if(check_div_seven(n) in [7,14,21,28,35,42,49,56,63,70,77,84,91,98]):
        divis.append(7)
    #by8
    if(check_div_eight(n) in [8,16,24,32,40,48,56,64,72,80,88,96]):
        divis.append(8)
    #by9
    if(sum_of_digits(n) in [9]):
        divis.append(9)
    #print(divis)
    
    if(len(divis) == 0):
        print("{} : is not divisible".format(n))
    else:
        res =""
        for c in divis:
            res = res + str(c)+ ","
        res = res[:-1]    
        print("{} : is divisible by {}".format(n,res))    
    
       
