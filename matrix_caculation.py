import numpy as np
import matplotlib.pyplot as plt
import rref

array = []
while True:
    line = input()
    if not line:
        break
    x, y = map(int, line.split())
    array.append((x, y))

n = len(array)
r = n-1

augmented_matrix = []

for x, y in array:
    row = [x**i for i in range(r+1)]
    row.append(y)
    augmented_matrix.append(row)

A = np.array(augmented_matrix, dtype=float)
# print(A, "\n")
A_ = rref.rref(A)
print(A_, "\n")
result = A_[:, -1]

print("k =", result[0])
for i in range(1, len(result)):
   print(f"a{i} = {result[i]}")

max_x = max(array, key=lambda x: x[0])[0]
min_x = min(array, key=lambda x: x[0])[0] * 0.9

x = np.linspace(min_x, max_x, 100)
y = np.polyval(result[::-1], x)
plt.plot(x, y)
plt.scatter(*zip(*array))
plt.show()