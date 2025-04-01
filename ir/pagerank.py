#page rank
import numpy as np

M = np.matrix([[0, 1, 1],
               [1/2, 0, 0],
               [1/2, 0, 0]])

dp = 1/3
E = np.zeros((3, 3))
E[:] = dp
print("E:\n", E)

beta = 0.5
A = beta * M + ((1-beta) * E)
print("A:\n", A)

r = np.matrix([dp, dp, dp])
r = np.transpose(r)
prev_r = r
iteration = 0
while True:
    r = A * r
    print(f"Iteration {iteration}:\n", r)
    if np.allclose(prev_r, r, atol=1e-6):
        break
    prev_r = r
    iteration += 1

print('final r:\n', r)
print('Sum of r:', sum(r))
