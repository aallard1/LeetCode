def defangIPaddr(address):
    newAddress = address.replace('.', '[.]', 3)
    return newAddress

print(defangIPaddr('1.1.1.1'))


# Runtime: 31 ms, faster than 51.04% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14.2 MB, less than 64.78% of Python3 online submissions for Defanging an IP Address.