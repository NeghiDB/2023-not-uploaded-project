import panda as pd
import numpy as np

data = {'item':['pencil','eraser','pen','laptop'],'price':[50,60,100,20]}
frame = pd.DataFrame(data)
print(frame.iloc[:3])