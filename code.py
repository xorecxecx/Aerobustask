import math
import sys
x, a, b = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
sm = (40-a)*x + (120-b)*x/2
print(math.floor(sm))
