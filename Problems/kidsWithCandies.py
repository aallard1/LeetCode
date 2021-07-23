class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxC = self.maxx(candies)
        isGreatest = []
        for i in range(len(candies)):
            if ((candies[i] + extraCandies) >= maxC):
                isGreatest.append(True)
            else:
                isGreatest.append(False)
        return isGreatest
    
    def maxx(self, candies):
        max_value = candies[0]
        for i in range(1, len(candies)):
            if (candies[i] > max_value):
                max_value = candies[i]         
        return max_value
