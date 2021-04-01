class Solution(object):  # By CyFun
    def maxProfit(self, prices):
        mintn = 100000
        btpro = 0
        for price in prices:
            if mintn > price:
                mintn = price
            elif btpro < price-mintn:
                btpro = price - mintn
        return btpro
