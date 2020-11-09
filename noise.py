# File: noise.py
# By: Huy
# Noise visualizer

import random

NUMS_TO_GENERATE = 100
MIN = 1
MAX = 100
nums = []

for _ in range(NUMS_TO_GENERATE):
    nums.append(random.randint(MIN, MAX))

print(nums)
