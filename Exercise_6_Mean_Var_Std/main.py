# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  list_to_array = np.array((list),3,axis=0)



print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)