import copy
import random

class Hat:
  def __init__(self, **kwarg):
    self.contents = []
    for key,value in kwarg.items():
        for i in range(value):
          self.contents.append(key)

  def draw(self, number):
    ball_sample = []
        
    if number >= len(self.contents):
      return self.contents

    for i in range(number):
      picked = random.choice(self.contents)
      ball_sample.append(picked)
      self.contents.pop(self.contents.index(picked))
    return ball_sample

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    sample = hat_copy.draw(num_balls_drawn)
    
    success = True
    for key in expected_balls.keys():
      if sample.count(key)<expected_balls[key]:
        success = False
        break
    if success:
      count += 1

  return count / num_experiments