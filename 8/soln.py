import sys
import numpy as np
import matplotlib.pyplot as plt

inp = open("input.txt")

lines = inp.readlines()
line = lines[0].strip("\n")
digits = [int(i) for i in str(line)]
digits = np.array(digits)
width = 25
height = 6
layers = len(digits) // (width * height)
image = digits.reshape(layers, height, width)
zeros = []
for i in range(layers):
    layer = image[i, :, :]
    zeros.append(np.count_nonzero(layer == 0))

#  import pdb; pdb.set_trace()
l = zeros.index(min(zeros))
layer = image[l, :, :]
ones = np.count_nonzero(layer==1)
twos = np.count_nonzero(layer==2)
print(ones * twos)
final_image = np.zeros((height, width))

for i in range(width):
    for j in range(height):
        vec = image[:, j, i]
        pos = np.argmax(vec!=2)
        final_image[j, i] = vec[pos]

print(final_image)
plt.imshow(final_image)
plt.show()

#  np.argmax
