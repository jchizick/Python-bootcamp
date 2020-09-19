import numpy as np

def calculate(list):
  if len(list)!= 9:
    raise ValueError("List must contain nine numbers.")
  x = np.array(list).reshape((3,3))
  calculations = {
  "mean": [x.mean(0).tolist(), x.mean(1).tolist(), x.mean()], 
  "variance": [x.var(0).tolist(), x.var(1).tolist(), x.var()],
  "standard deviation": [x.std(0).tolist(), x.std(1).tolist(), x.std()],  
  "max": [x.max(0).tolist(), x.max(1).tolist(), x.max()], 
  "min": [x.min(0).tolist(), x.min(1).tolist(), x.min()],  
  "sum": [x.sum(0).tolist(), x.sum(1).tolist(), x.sum()] 
  }
  return calculations
