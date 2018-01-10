# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 08:37:42 2017

@author: Micha
"""

a="rjsfd;ljsfkgjkagjajkgkadgrovmdafdkjgakdfjg9485;lfjkdfamferm4tmukejghjrr3urjevnnvjaschsIE&(!@#498e7JpGAgaNR4T94UDJAE289493rrkgjkamf;e;gorpdc,ew,dewif"
class Solution(object):
    def lengthOfLongestSubstring(self, a):
    # :type a: str
    # :rtype: int
        """ returns longest substring of a without a repeating char """
        L=len(a)
        if L==0:
            return L
        k=1
        stCur=0 #index of starting position of current string
        stBest=0 #index of starting position of best string
        bestLength=1
        currentLength=1
    
        while k<L:  # for each element in a
            m=0
            flag=True
            curChar=a[k]
            while m<currentLength and flag:
                if a[stCur+m]==curChar:
                    flag=False
                    stCur=m+1+stCur
                    currentLength=currentLength-(m+1)+1
                m+=1
            if flag==True:
                currentLength+=1
            if currentLength>bestLength:
                stBest=stCur
                bestLength=currentLength
            k+=1
            if L-k + currentLength<bestLength:
                return bestLength
        #bestString=a[stBest:stBest+bestLength]
        return bestLength
            
    
    