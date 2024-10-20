import pandas as pd
import numpy as np

#列表创建
a=[2,3,5,6,7,8]
s=pd.Series(a)
print(s)

a = ["Google", "Runoob", "Wiki"]
s = pd.Series(a, index = ["x", "y", "z"])
print(s[1])