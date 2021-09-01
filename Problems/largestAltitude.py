def largestAltitude(gain):
    altitude = []
    altitude.append(0)
    for i in gain:
        altitude.append(altitude[-1] + i)
    maxAlt = max(altitude)
    return maxAlt

# Runtime: 40 ms, faster than 18.50% of Python3 online submissions for Find the Highest Altitude.
# Memory Usage: 14 MB, less than 97.81% of Python3 online submissions for Find the Highest Altitude.