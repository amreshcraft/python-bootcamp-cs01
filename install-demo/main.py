import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6]])

# Save to a text file
np.savetxt('data.txt', data, fmt='%d', delimiter=',')

# Load back from the text file
loaded_txt = np.loadtxt('data.txt', delimiter=',')

print("Loaded Text Data:\n", loaded_txt)