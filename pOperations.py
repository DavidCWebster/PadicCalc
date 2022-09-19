# P-adic operations and P-adic Class
import math
import basesMod


def complement(num,P):
        if num>10 or num>P:
            print("something went wrong ding dong")
        x= P-1-num
        return x


def extend(lst):
    newlst=lst[:]
    newlst.extend(lst)
    return newlst




#######################################################DECIMAL###########################################333333####################
class decimal:
    def __init__(self,repeater,nonRepeat):
        self.repeater= repeater
        self.nonRepeat= nonRepeat

        # self.repeater=list(self.repeater.split())
        # self.nonRepeat=list(self.nonRepeat.split())
        



    # def __str__(self):
    #     strRepeater = ''.join(str(x) for x in self.repeater)
    #     strNonRepeat = ''.join(str(x) for x in self.nonRepeat)

    #     tString=""
    #     tString+="{}({})"
    #     tString=tString.format(strNonRepeat, strRepeater)
    #     return tString

    def DtoP(self, P):
        Re=self.repeater.res[:]
        nRe=self.nonRepeat.res[:]

        print(Re,"repeater")
        print(nRe)
        
        nRe=basesMod.clean(nRe)
        print(nRe)
        print("#####")



        for i in range(len(self.repeater.res)):
            if Re[i]==0:
                continue
            Re[i]=complement(Re[i],P)
        for i in range(len(nRe)):
            xRe=extend(Re)
            if nRe[i]==0:
                pass
            nRe[i]=complement(xRe[i],P)

        print(Re)
        print(nRe)



        if len(Re)==0:
            nRe=Re

            for i in range(len(nRe)):
                if nRe[-(i+1)]<P:
                    nRe[-(i+1)]+=1
                    break
                else:
                    nRe[-(i+1)]=0

        
        numRe= int(''.join(map(str,Re)))
        numnRe=  int(''.join(map(str,nRe)))

        numRe=basesMod.base(numRe,P)
        numnRe=basesMod.base(numnRe,P)


        padic=pInt(numRe,numnRe,P)

        return padic
       
       
            
            






    






    def convertFra2(numerator, denominator,):

        negative = False

        if denominator == 0:
            return 'Undefined'
        if numerator == 0:
            return '0'
        if numerator*denominator < 0:
            negative = True
        if numerator % denominator == 0:
            return str(numerator/denominator)
    
        num = abs(numerator)
        den = abs(denominator)

        result = ""
        nonrepeat=""
        nonrepeat+=str(num//den)
        nonrepeat+="."
        result += str(num // den)
        result += "."
        repeater=""
        

        quotient_num = []
        while num:
    	    # In case the remainder is equal to zero, there are no repeating
            # decimals. Therefore, we don't need to add any parenthesis and we can
            # break the while loop and return the result.
            remainder = num % den
            if remainder == 0:
                for i in quotient_num:
                    result += str(i[-1])
                break
            num = remainder*10
            quotient = num // den

		    # If the new numerator and quotient are not already in the list, we
            # append them to the list.
            if [num, quotient] not in quotient_num:
                quotient_num.append([num, quotient])
            # If the new numerator and quotient are instead already in the list, we 
            # break the execution and we prepare to return the final result.
            # We take track of the index position, in order to add the parenthesis 
            # at the output in the right place.
            elif [num, quotient] in quotient_num:
                index = quotient_num.index([num, quotient])
                for i in quotient_num[:index]:
                    nonrepeat+=str(i[-1])
                    result += str(i[-1])
                result += "("
                
                for i in quotient_num[index:]:
                    result += str(i[-1])
                    repeater+=str(i[-1])
                result += ")"

                break
    
        infDec= decimal(repeater, nonrepeat)
        return infDec

#######################################################################################################################################FRACTION
class fraction:
    def __init__(self,numerator,denominator):
        self.numerator= numerator
        self.denominator= denominator

    def __str__(self):
        stringver= f'{self.numerator}/{self.denominator}'
        return stringver

    def __add__(self,o):
        yuh=0

        lcm= basesMod.LCM(self.denominator, o.denominator)

        sfactor=lcm//self.denominator
        newsnum=sfactor*self.numerator
        
        ofactor=lcm//o.denominator
        newonum=ofactor*o.numerator

        sum=newonum+newsnum
        den=lcm

        newfrac=fraction(sum,den)
        return newfrac

    def __mul__(self,o):
        num=self.numerator*o.numerator
        den=self.numerator*o.denominator

        frac=fraction(num,den)
        return frac

    def __sub__(self,o):
        yuh=0
        

    
    def convertFra(self, P):
        numerator=self.numerator
        denominator=self.denominator
        negative = False

        

        zero=basesMod.base([0],numerator.base)

        if abs(denominator) == "0":
            return 'Undefined'
        if abs(numerator) == "0":

            print("hello")
            
            return decimal(zero,zero)


        # if numerator*denominator < 0:
        #     negative = True
        if abs(numerator % denominator) == "0":
            return decimal(zero,numerator//denominator)
    
        num = numerator
        den = denominator


        

        result = ""
        nonrepeat=""
        nonrepeat+=str(num//den)
        nonrepeat+="."
        result += str(num // den)
        result += "."
        repeater=""
        

        quotient_num = []
        while abs(num)=="0":
    	    # In case the remainder is equal to zero, there are no repeating
            # decimals. Therefore, we don't need to add any parenthesis and we can
            # break the while loop and return the result.
            remainder = num % den
            if remainder == 0:
                for i in quotient_num:
                    result += str(i[-1])
                break
            num = remainder*basesMod.base([1,0],num.base)
            quotient = num // den

		    # If the new numerator and quotient are not already in the list, we
            # append them to the list.
            if [num, quotient] not in quotient_num:
                quotient_num.append([num, quotient])
            # If the new numerator and quotient are instead already in the list, we 
            # break the execution and we prepare to return the final result.
            # We take track of the index position, in order to add the parenthesis 
            # at the output in the right place.
            elif [num, quotient] in quotient_num:
                index = quotient_num.index([num, quotient])
                for i in quotient_num[:index]:
                    nonrepeat+=str(i[-1])
                    result += str(i[-1])
                result += "("
                
                for i in quotient_num[index:]:
                    result += str(i[-1])
                    repeater+=str(i[-1])
                result += ")"

                break
    
        repeater=basesMod.base(repeater, numerator.base)
        nonrepeat=basesMod.base(nonrepeat,numerator.base)

        infDec= decimal(repeater, nonrepeat)



        return infDec    


##################################################################################################################################################pINT

class pInt:
    def __init__(self,repeater,nonRepeat, P):
        self.repeater= repeater
        self.nonRepeat= nonRepeat
        self.P=int(P)
        

    def shiftleft(self, num):

        newList=self.nonRepeat.res[:]

        for i in range(num):
            newList.append(0)
        
        return basesMod.base(newList,self.nonRepeat.base)

    def __str__(self):
        string=f'{self.repeater}${self.nonRepeat}'
        return string
        




    def PtoF(self):
        yuh=0
        nonRepeatD= self.nonRepeat
        
        # x=nonRepeatD*(pow(self.P,len(self.repeater)))
        # y=nonRepeatD*(pow(self.P,len(self.nonRepeat)))
        # y+=pow(self.repeater,len(self.nonRepeat))

        x= self.shiftleft(3)
        y=self.shiftleft(1)

        print(x)
        print(y)
        
        y.res.insert(0,self.repeater.res[-1])

        if len(self.repeater.res)==1:
            y.res.insert(0,self.repeater.res[-1])
        else:
            y.res.insert(0,self.repeater.res[-2])



        numerator= x-y
        denominator=basesMod.base([1,0,0,0],self.P)-basesMod.base([1,0],self.P)
        gcd= basesMod.GCD(numerator,denominator)
        numerator=numerator//gcd
        denominator=denominator//gcd

        frac=fraction(numerator,denominator)
        
        return frac


    def __add__(self,o):
        yuh=0
        P=self.P
        if P!=o.P:
            print("something went wrong with the bases")
        
        this=pInt.PtoF(self)
        other=pInt.PtoF(o)

        print(this)
        print(other)

        frac=this+other

        print(frac)
        dec=fraction.convertFra(frac, P)

        

        padic=decimal.DtoP(dec, P)
        

        return padic

    

    
















    




    













