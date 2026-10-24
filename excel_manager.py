import pandas as pd

data= pd.read_excel("جدول_فروش_کالاها.xlsx")
data_list=data.to_dict("records")

