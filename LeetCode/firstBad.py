# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 21:35:51 2017

@author: zhang_000
"""

#First Bad Version
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return ''
        lessThan20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        lessThan20.append('')   
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        if num < 20:
            return lessThan20[num-1]
        if num < 100:
            return (tens[num/10 - 2] + ' ' + self.numberToWords(num%10)).rstrip()
        if num < 1000:
            return (lessThan20[num/100-1] + ' Hundred ' + self.numberToWords(num%100)).rstrip()
         
        for p, w in enumerate((' Thousand ', ' Million ', ' Billion '), 1):
            if num < 1000**(p+1):
                return (self.numberToWords(num/1000**p) + w + self.numberToWords(num%1000**p)).rstrip
           
            