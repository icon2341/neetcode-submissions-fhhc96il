class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) <2):
            return 0
        p1 = 0
        p2 = 1
        profit = 0
        p2SeenLowest= min(prices[p1], prices[p2])

        while(p1 < p2 and p1 < len(prices)-1 and p2 < len(prices)):
            calcedProfit = prices[p2] - prices[p1]
            if(calcedProfit > profit):
                profit = calcedProfit

            # always keeping track of the cheapest number p2 has seen.
            if(prices[p2] < p2SeenLowest):
                p2SeenLowest = prices[p2]
            # move p2 up 1
            p2 += 1
            # to determine if we move p1 up 1, we need to know if there is
            # a better buy opportunity, this could be determined via what p2 has "seen"
            while prices[p1] > p2SeenLowest:
                print(p1, p2SeenLowest, prices[p1])
                p1 += 1
        return profit

