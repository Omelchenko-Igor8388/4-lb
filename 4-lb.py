import pandas as pd

dataFilel = pd.read_excel(r"C:\Users\Satellite\Desktop\4\laba.xlsx")
dataFilel = pd.DataFrame(dataFilel, index=[0,1,2,3,4,5,6,7,8,])
print(dataFilel)
