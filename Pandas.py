# Pandas DataSeries
# a) Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
# b) Write a Pandas program to convert a Panda module Series to Python list and it's type

# Code for a:

import pandas as pd
import numpy as np 

data_list = pd.Series([1,2,3,4,5])

print(data_list)

# Output for a:

# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# Code for b:

import pandas as pd
import numpy as np 

data_list = pd.Series([1,2,3,4,5])

print(data_list)

data_list = data_list.tolist()


print(data_list)

# Output for b: 

# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64
# [1, 2, 3, 4, 5]

