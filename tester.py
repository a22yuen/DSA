import os
import random
d = random.choice(os.listdir("./"))
print(random.choice(os.listdir(f'./{d}/')))
