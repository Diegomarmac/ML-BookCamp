import numpy as np


#### Sorting

# let's generate a one dimensional array with four elements
pred = np.random.rand(4).round(2)

# to create a sorted copy of the array:
np.sort(pred)

# if we want to sort the elements of the array without creating another:
pred.sort()

# another useful thing: argsort, it returns the indices of the array in the sorted order
idx = pred.argsort()

# now we can use the array idx with indexes to get the original array in the sorted order
pred[idx]

#### Re shaping and combining
rng = np.arange(12)

# it's possible to change the shape, using reshape
rng.reshape(4,3)

# the reshaping worked because it was possible to rearrange 12 original elements, if we attempt to reshape it to (4,4) it won't let us


# sometimes we need to create a new NumPy array by putting multiple arrays together
vec = np.arange(3)
mat = np.arange(6).reshape(3,2)

# the simplest way to combine two NumPy arrays:
np.concatenate([vec,vec])

# we can achieve the same result using horizontal stack:
np.hstack([vec,vec])

# and the same with two-dimensional arrays
hp.stack([mat,mat])

# however, in case of two dimensional arrays np.concatenate works diffenrently from np.hstack
np.concatenate([mat,mat])
# concatenate do it horizontally

# now, imagine we want to add an extra column to our matrix:
# for that we simply pass a list that contains the vector and then the matrix
np.column_stack([vec,mat])

# we can apply np.column_stack t otwo vectors
np.column_stack([vec, vec])

# there's np.vstack that stacks arrays vertically
np.vstack([vec,vec])

# eith matrices the result is the same as np.concatenate
np.vstack([mat,mat])

# np.vstack function can also stack together vectors and matrices
np.vstack([vec,mat.T])
# mat.T es la matriz transpuesta de mat


####### Slicing and filtering
# like with lists we can also use slicing
mat = np.arange(15).reshape(5,3)

# for example to get the first 3 rows
mat[:3]
mat[1:3]

# for columns
mat[:, :2]
# Here we have two ranges
# The first one is simply a colon : with no start and no end, which means "include all rows"
# The second one is a range that includes columns 0 and 1 (2 not included)

# we can combine both and select any matrix part we want
mat[1:3, :2]

# if we don't need a range, but rather some specific rows or columns we can simply provide a list of indices:
mat[[3,0,1]]

# suposse  we want to choose rows where the first element of a row is an odd number
# 1. Select the first column of the matrix
# 2. Apply the mod 2 operations to all the elemetns to compute the remainder of the division by 2
# 3. if the remainder is 1, then the number is odd, and if 0 the number is even

# this in code is:
mat[:, 0] % 2 == 1

# now we can use this expression to select only rows where the expression is True
mat[mat[:, 0] % 2 == 1] # traeme los renglones donde el primer elemento de cada renglón es impar
