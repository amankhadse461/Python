a, b = 2, 3
(a ** b) # = 8
pow(a, b) # = 8
import math
math.pow(a, b) # = 8.0 (always float; does not allow complex results)
import operator
operator.pow(a, b) # = 8