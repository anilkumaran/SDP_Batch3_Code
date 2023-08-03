#divisibility rule
def divisible(elements):
    for n in elements:
        L=[1]
        if n[-1] in ["0","2","4","6","8"]:
            L.append(2)
        def dby3(n):
            sum_digits=0
            if len(n)==1:
                if n in ["3","6","9"]:
                    L.append(3)
                    return L
            else:
                for i in n:
                    sum_digits = sum_digits+int(i)
                dby3(str(sum_digits))
        dby3(n) 
        if len(n)>1:
            if n[-2] in ["0","2","4","6","8"] and n[-1] in ["0","4","8"]:
                L.append(4)
            if n[-2] in ["1","3","5","7","9"] and n[-1] in ["2","6"]:
                L.append(4)
        elif n in ["4","8"]:
            L.append(4)
        if n[-1] in ["0","5"]:
            L.append(5)
        if 2  in L and 3 in L:
            L.append(6)
        def dby7(n):
            if len(n)==1:
                if n in ["0","7"]:
                    L.append(7)
                    return L
            else:
                last=int(n[-1])
                first=int(n[:-1])
                diff=abs(first-last*2)
                diff=str(diff)
                return dby7(diff)
        dby7(n)
        def dby8(n):
            if len(n)==1:
                if n in ["0","8"]:
                    L.append(8)
                    return L
            else:
                first=int(n[:-1])*2
                result=int(n[-1])+first
                return dby8(str(result))
        dby8(n)
        def dby9(n):
            sum_digits=0
            if len(n)==1:
                if n in ["9"]:
                    L.append(9)
                    return L
            else:
                for i in n:
                    sum_digits=sum_digits+int(i)
                    dby9(str(sum_digits))
        dby9(n)          
        Req=",".join(map(str,L))
        print("{0} is divisible by {1}".format(n,str(Req)))
elements=input("enter the elements:").split(",")
L=divisible(elements)
