import numpy as np

# NumPy delegates all the internal computations to BLAS and LAPACK for efficient low-level computations, and this is why it's blazingly fast

########### VEctor vector multiplication
# If we have two NumPy arrays U and V, the dot product between them is:
dot = 0

for i in range(n):
    dot = u[i] * v[i]

# using NumPy Operations we can doit with one line expression
(u * v ).sum()

# however, there's implemented inside NumPy in the dot method
u.dot(v)

# matrix vector multiplication

v = np.zeros(m)

for i in range(m):
    v[i] = X[i].dot(u)

# we can use the dot method of the matrix X to multiply it by vector U
v = X.dot(u)

