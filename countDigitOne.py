class Solution:
    def countDigitOne(self, x):
        """
        :type x: int
        :rtype: int
        Return the total number of ones in non-neg integers less than or equal to x
        #leetCode problem #233 in algorithms
        """
        if x<=0:
            return 0
          
        k=1
        c=0
        
        baseArray=[1]
        while k<=x:              
            k=k*10
            c=c+1
            #baseArray[c]=k
            baseArray.append(k)
      #  print(baseArray)
      #  print(c)
        powBase=c-1
        base=baseArray[powBase]
        baseD=baseArray[powBase-1]
       # print(base)
       # cc=self.numOnes_noRecurse(powBase)
        out=0
        
        if base==x:
            return out+(baseD*powBase ) +1     #baseB*powBase is total number of ones for numbers < base
        while x>0:
            if x<10:
                out+=1
                return out       
  
            q=x//base  #always <10
            r=int(x-q*base)        
            if q==0:
                powBase+=-1
                base=baseD
                baseD=baseArray[powBase-1]
                continue
            elif q==1:
                out+=(baseD*powBase)+1  #add <= q*10^powBase 
                if r>9 or r==0:
                    out+=r
                else:
                    out+=(r+1)
                    return out
            elif q>1:
                out+= base+(q)*(baseD*powBase)  #add <= q*10^powBase
            x=r
            powBase+=-1
            base=baseD
            baseD=baseArray[powBase-1]
        return out
    