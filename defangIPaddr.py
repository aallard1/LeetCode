def defangIPaddr(address):
    newAddress = address.replace('.', '[.]', 3)
    return newAddress

print(defangIPaddr('1.1.1.1'))