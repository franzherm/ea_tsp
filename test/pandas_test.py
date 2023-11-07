import numpy as np
import pandas as pd

# Sample 3D array (replace this with your actual data)
data = np.random.randint(0, 10, size=(2, 3, 4))
print("Data: \n",data,"\n")
# Get the shape of the array
shape = data.shape

# Create a multi-index
multi_index = pd.MultiIndex.from_product([range(shape[0]), range(shape[1])], names=['experiment', 'iteration'])

# Reshape the data to 2D
reshaped_data = data.reshape(-1, shape[2])
print("Reshaped data: \n",reshaped_data,"\n")
# Create DataFrame with multi-index
df = pd.DataFrame(reshaped_data, index=multi_index, columns=range(shape[2]))

# Display the DataFrame
print(df)