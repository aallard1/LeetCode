def maximumWealth(accounts):
    customerWealth = []
    for i in accounts:
        customerWealth.append(sum(i))         
    return max(customerWealth)

maximumWealth([[1,2,3,4],[5,1,2,7]])