def maximumWealth(accounts):
    customerWealth = []
    for i in accounts:
        customerWealth.append(sum(i))         
    return max(customerWealth)

maximumWealth([[1,2,3,4],[5,1,2,7]])


# Runtime: 127 ms, faster than 5.02% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 14.2 MB, less than 59.91% of Python3 online submissions for Richest Customer Wealth.