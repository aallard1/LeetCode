def largestAltitude(gain):
    altitude = []
    altitude.append(0)
    for i in gain:
        altitude.append(altitude[-1] + i)
    maxAlt = max(altitude)
    return maxAlt