import math


S_old = 205
S_new = 196

T = [0.5, 4, 13]
for T_i in T:
    prob = math.exp(-(S_old - S_new) / T_i)
    print(prob)
