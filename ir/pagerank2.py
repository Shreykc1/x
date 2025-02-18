# import some stuff
import numpy as np

from fractions import Fraction

# keep it clean and tidy
def float_format(vector, decimal):
    return np.round((vector).astype(float), decimals=decimal)


dp = Fraction(1,3)
print(dp)
# WWW matrix
M = np.matrix([[0,Fraction(1,2),Fraction(1,2)],
        [1,0,0],
        [1,0,0]])
print(M)

E = np.zeros((3,3))
E[:] = dp

# taxation
beta = 0.5

# WWW matrix
A = beta * M + ((1-beta) * E)
print(A)

# initial vector
r = np.matrix([dp, dp, dp])
r = np.transpose(r)

previous_r = r
for it in range(1,100):
    r = A * r
    print(float_format(r,3))
    #check if converged
    if (previous_r==r).all():
        break
    previous_r = r

print("Final:\n", float_format(r,3))
print("sum", np.sum(r))
