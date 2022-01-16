import numpy as np

# Numpy arrays are similar ti PYthon lists, but they are better optimized for number crunching tasks

# To create an array of a predefined size filled with zeros:
zeros = np.zeros(10) # this creates an array with 10 zero elements

ones = np.ones(10) # the same as zeros, ezcept the elements are ones

# Both functions are shortcut for np.fill
# if we wanna create an array of size 10 filled with zeros:
array = np.fill(10,0.0)

# and we can create the same result using np.repeat
array = np.repeat(0.0, 10)

# np.repeat is more powerful
array = np.repeat([0.0,1.0], 5)
# it creates an array of size 10, where each number, 0 and 1 are repeated 5 times

# and also is more flexible:
array = np.repeat([0.0, 1.0], [2,3])
# this code is gonna create an array size 5, with 2 zeros and three ones


el = array[1]

# We can acces multiple elements at the same time
array[[4,2,0]]

# if we have a list with numbers, we can convert it to a NumPy array
elements = [1, 2, 3, 4]
array = np.array(elements)

# another useful function for creating Numpy arrays is np.arange
np.arange(10) # it creates an array of length 10 with numbers from 0 to 9

# create an array of certain size, filled with numbers between some number x and some number y
thresholds = np.linspace(0,1, 11)
# the starting number here is 0
# to 1, the second one in the function
# length of the resulting array

# we can specify the dtype
zeros = np.zeros(10, dtype=np.uint8) # aquí estamos especificando un unsigned int de 8 bits

# one dimensional NumPy arrays are vectors, for ML we need often matrices

zeros = np.zeros((5,2), dtype=np.float32)
# here we are creating an array of 5 rows and 2 columns

# the dimensionality of an array is called shape
zeros.shape

numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

numbers = np.array(numbers) # here we are converting a list of lists to a np.array

# to get the entire row
numbers[0]

# to acces a columns of a two dimensional array:
numbers[:,1]

# it's possible to overwrite the content of the entire row or a column
numbers[1] = [1,1,1]
numbers[:,2] = [9,9,9]

#### RAndomly generated arrays
arr = np.random.rand(5,2) # generate a 5 x 2 array of random numbers uniformly distributed between 0 and 1

# this generates a different result everytime we run the code

# to make it reproducible we use seeds
np.random.seed(2)
arr = np.random.rand(5,2)

# if we want to sample from the standard normal distribution
arr = np.random.randn(5,2)

# to generate uniformly distributed random integers between 0 and 100
randint = np.random.randint(low=0, high=100, size=(5,2))

## Shuffle
idx = np.arange(5)
np.random.suffle(idx)

###################
### NumPy Operations
###################

rng = np.arange(5)

# to multiply every element of the array by two, we simply use the multuplication operator
rng * 2
# this is the smae with + , - and /
# it's possible apply multiple operations

(rng - 1) * 3 / 2 + 1

# also it's possible make operations with two arrays of the same shape
noise = 0.01 * np.random.rand(5)
numbers = np.arange(5)

result.round(4)

# sometimes we need to sqare all the elements of an array
# for that, we can multiply the array by itself
# let's first generate an array
pred = np.random.rand(3).round(2)
square = pred * pred
# or we can use the power operator
square = pred ** 2

pred_exp = np.exp(pred) # computes the exponent
pred_log = np.log(pred) # computes the logarithm
pred_sqrt = np.sqrt(pred) # computes the square root

### Boolean operations
# let's create an array with some random numbers
pred = np.random.rand(3).round(2)
result = pred >= 0.5

# as with arithmetic operations we can apply boolean operations on two NumPy arrays
pred1 = np.random.rand(3).round(2)
pred2 = np.random.rand(3).round(2)
pred1 >= pred2 # this give us an array of booleans

########################
# Summarizing operations
#########################

# let's create an array anf the ncalculate the sum of all elements
pred = np.random.rand(3).round(2)
pred_sum = pred.sum()

# and we can get min,mean and max
pred.min()
pred.mean()
pred.max()
pred.std()

# now, let's create a MAtrix
matrix = np.random.rand(4,3).round(2)

# si queremos obtener el max de cada renglón usamos:
matrix.max(axis = 1)
# si quisieramos el max de cada columna:
matrix.max(axis = 0)

# other operations sum,min,mean,std can take acis as an argument
matrix.sum(axis = 1)