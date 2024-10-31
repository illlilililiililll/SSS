import numpy as np

x = []
y = []
print("Enter x and f(x) pairs (empty line to finish):")
while True:
    line = input()
    if not line:
        break
    x0, y0 = map(int, line.split())
    x.append(x0)
    y.append(y0)

n = len(x) - 1

coef = np.zeros(n+1)
for i in range(n+1):
    t_coef = np.array([1])
    for j in range(n + 1):
        if i != j:
            t_coef = np.convolve(t_coef, [1, -x[j]]) / (x[i] - x[j])
    coef += y[i] * t_coef

coef = coef[::-1]
print("k =", coef[0])
for i in range(1, len(coef)):
   print(f"a{i} = {coef[i]}")