"""
- Calculation of probabilistic momentums -
Author: Genaro Martínez A01566055
date: 01/13/20
"""
def calculateFreq(list):
    d = {x:list.count(x) for x in list}
    return d

def calculateProb(size, frequencies):
    values, keys = list(frequencies.values()), list(frequencies.keys())
    print(values)
    print(keys)
    arr = [values[i] / size for i in range(len(values))]
    return arr

data_x = input("Ingrese los datos ")
data_x = data_x.split(" ")
data_y = list(map(int, data_x))
size = len(data_y)
data_y.sort()

frequencies = calculateFreq(data_y)
keys = list(frequencies.keys())
probabilities = calculateProb(size, frequencies)

print (frequencies)
print (probabilities)
m1 = 0
m2 = 0
m3 = 0
m4 = 0
var = 0
for k in range(0, len(keys)):
    m1 += keys[k] * probabilities[k]
    m2 += (keys[k] ** 2) * probabilities[k]
    m3 += (keys[k] ** 3) * probabilities[k]
    m4 += (keys[k] ** 4) * probabilities[k]

var = m2 - (m1**2)

print("m1:", m1)
print("m2:", m2)
print("m3:", m3)
print("m4:", m4)
print("var:", var)
