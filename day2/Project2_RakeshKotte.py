def divisible_by8(nums):
    if len(nums) == 1:
        return nums
    else:
        if len(nums) > 2 and nums[-3] in ["1","3","5","7","9"]:
            res = int(nums[:-1]) + 4
            res = str(res)
        else:
            res = nums[-2:]
        a = (int(res[:-1]))*2+int(res[-1])
        return divisible_by8(str(a))

def divisible_by7(nums):
    if len(nums) == 1:
        return nums
    else:
        last_digit = int(nums[-1])
        remaining = int(nums[:-1])
        res = abs(last_digit*2 - remaining)
        res = str(res)
        return divisible_by7(res)



def divisible_by_4(nums):
    if len(nums) == 1 and nums in ["4","8"]:
        return True
    elif len(nums) > 1 and nums[-2] in ["1","3","5","7","9"] and nums[-1] in ["2","6"]:
        return True
    elif len(nums) > 1 and nums[-2] in ["0","2","4","6","8"] and nums[-1] in ["0","4","8"]:
        return True
    else:
        return False
def divisible_by_3(nums):
    if len(nums) == 1:
        return nums
    else:
        num_list = list(map(int,nums))
        su = 0
        for i in num_list:
            su += i
        a = str(su)
        return divisible_by_3(a)
    
l = input().split()
for i in l:
    try:
        res = ""
        divisible_by2 = i[-1] in ["0","2","4","6","8"]
        divisible_by3 = divisible_by_3(i) in ["3","6","9"] 
        divisible_by_9 = divisible_by_3(i) =="9"
        if divisible_by2:
            res += "2"
        if divisible_by3:
            res += "3"
        if divisible_by_4(i):
            res += "4"
        if i[-1] in ["0","5"]:
            res += "5"
        if divisible_by2 and divisible_by3:
            res += "6"
        if divisible_by7(i) in ["0","7"]:
            res+="7"
        if divisible_by8(i) == "8":
            res += "8"
        if divisible_by_9:
            res += "9"
        a = ",".join(res)
        print(i,": is divisible by {}".format(a))
    except:
        print(i,": Invalid Number")
