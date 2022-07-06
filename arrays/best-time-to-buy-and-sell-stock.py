def maxProfit(self, prices):
    buying_price = prices[0]
    max_profit = 0
    
    for i in range(len(prices)):
        if buying_price > prices[i]:
            buying_price = prices[i]
        elif (prices[i] - buying_price) > max_profit:
            max_profit = prices[i] - buying_price
    return max_profit