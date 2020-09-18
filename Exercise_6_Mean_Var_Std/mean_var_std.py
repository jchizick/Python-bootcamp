import numpy as np

def calculate(list):
  if len(list)!= 9:
    raise ValueError("List must contain nine numbers.")
  x = np.array(list).reshape((3,3))
  calculations = {
  "mean": [x.mean(0).tolist(), x.mean(1).tolist(), x.mean().tolist()], 
  "variance": [x.var(0).tolist(), x.var(1).tolist(), x.var().tolist()],
  "standard deviation": [x.std(0).tolist(), x.std(1).tolist(), x.std().tolist()],  
  "max": [x.max(0).tolist(), x.max(1).tolist(), x.max().tolist()], 
  "min": [x.min(0).tolist(), x.min(1).tolist(), x.min().tolist()],  
  "sum": [x.sum(0).tolist(), x.sum(1).tolist(), x.sum().tolist()] 
  }
  return calculations