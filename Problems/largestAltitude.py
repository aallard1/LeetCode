gain = [-5,1,5,0,-7]
newa = [0, -5, -4, 1, 1, -6]

def largestAltitude(gain):
    maxNum = 0
    temp = 0
    for i in gain:
        temp = maxNum + i
        if temp > maxNum:
            maxNum = temp
        temp = i
    
    return maxNum
           
print(largestAltitude(gain))

# def largestAltitude(gain):
#     altitude = [0]
#     while gain:
#         altitude.append(gain.pop(0)+altitude[-1])
#     return max(altitude)

# # Runtime: 46 ms, faster than 13.78% of Python3 online submissions for Find the Highest Altitude.
# # Memory Usage: 14 MB, less than 97.73% of Python3 online submissions for Find the Highest Altitude.

# def largestAltitude(gain):
#     altitude = [0]
#     for i in gain:
#         altitude.append(altitude[-1] + i)
#     return max(altitude)

# # Runtime: 36 ms, faster than 61.79% of Python3 online submissions for Find the Highest Altitude.
# # Memory Usage: 14.3 MB, less than 7.44% of Python3 online submissions for Find the Highest Altitude.

# # gain = [4,3,7,2]
# def largestAltitude(gain):
#     altitude = [0]
#     altitude.append(0)
#     for i in gain:
#         altitude.append(altitude[-1] + i)
#     maxAlt = max(altitude)
#     return maxAlt

# Runtime: 40 ms, faster than 18.50% of Python3 online submissions for Find the Highest Altitude.
# Memory Usage: 14 MB, less than 97.81% of Python3 online submissions for Find the Highest Altitude.

# a = [0,4,7,14,16]